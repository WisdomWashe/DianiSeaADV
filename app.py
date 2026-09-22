import os
import shutil
from datetime import datetime
from functools import wraps
from urllib.parse import urlencode

from flask import (
    Flask,
    abort,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.utils import secure_filename

import db
from data import CONTACT_INFO, FAQS, SEED_SAFARIS, TESTIMONIALS
from i18n import (
    DEFAULT_LOCALE,
    LOCALE_NAMES,
    SUPPORTED_LOCALES,
    resolve_locale,
    translate,
)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
UPLOAD_DIR = os.path.join(BASE_DIR, "static", "uploads")
COVERS_DIR = os.path.join(BASE_DIR, "static", "covers")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "gif"}

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key-change-this-in-production")
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB per request

os.makedirs(DATA_DIR, exist_ok=True)
app.config["DATABASE_PATH"] = os.environ.get(
    "DATABASE_PATH", os.path.join(DATA_DIR, "diani.db")
)

db.init_app(app)  # registers the connection-close hook

# Change this before deploying! Set ADMIN_PASSWORD as an environment
# variable in production rather than relying on the default below.
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "diani2026")


# ---------------------------------------------------------------------------
# Setup helpers
# ---------------------------------------------------------------------------

def ensure_upload_dirs(slugs):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    for slug in slugs:
        os.makedirs(os.path.join(UPLOAD_DIR, slug), exist_ok=True)


def bootstrap_database():
    """Create tables if missing, and seed the safaris on first run."""
    with app.app_context():
        db.init_db()
        if db.count_safaris() == 0:
            db.seed_safaris(SEED_SAFARIS)
        ensure_upload_dirs(db.get_all_slugs())


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# The only accent colors that actually have matching CSS classes
# (static/css/style.css). Adding a 7th means adding a new .accent-xxx
# rule there first.
ACCENT_CHOICES = ["lagoon", "ocean", "coral", "gold", "indigo", "sky"]


def blank_safari_raw():
    """An empty safari shape, for the 'add new safari' form - same
    structure get_safari_raw() returns for an existing one, just empty."""
    d = {"id": None, "slug": "", "accent": "lagoon", "emoji": "", "display_order": 0}
    for field in db.TRANSLATABLE_TEXT_FIELDS:
        d[field] = {loc: "" for loc in SUPPORTED_LOCALES}
    for field in db.TRANSLATABLE_LIST_FIELDS:
        d[field] = {loc: [] for loc in SUPPORTED_LOCALES}
    return d


def safari_to_form_values(raw):
    """Flatten a raw (unresolved, per-locale) safari dict into the same
    flat {field}_{locale} shape the edit form's inputs use, so the
    template can read e.g. form.name_en / form.itinerary_de directly."""
    values = {
        "id": raw["id"],
        "slug": raw["slug"],
        "accent": raw["accent"],
        "emoji": raw["emoji"],
        "display_order": raw["display_order"],
    }
    for field in db.TRANSLATABLE_TEXT_FIELDS:
        for loc in SUPPORTED_LOCALES:
            values[f"{field}_{loc}"] = raw[field].get(loc, "")
    for field in ("overview", "highlights", "included", "excluded", "bring"):
        for loc in SUPPORTED_LOCALES:
            values[f"{field}_{loc}"] = "\n".join(raw[field].get(loc, []))
    for loc in SUPPORTED_LOCALES:
        lines = [
            f"{stop.get('icon', '')} | {stop.get('title', '')} | {stop.get('description', '')}"
            for stop in raw["itinerary"].get(loc, [])
        ]
        values[f"itinerary_{loc}"] = "\n".join(lines)
    return values


def parse_itinerary_textarea(text):
    """Parse lines shaped 'icon | title | description' into stop dicts."""
    stops = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split("|", 2)]
        parts += [""] * (3 - len(parts))  # pad so short lines don't crash
        stops.append({"icon": parts[0], "title": parts[1], "description": parts[2]})
    return stops


def build_itinerary_field(form):
    """
    Combine the three itinerary_<locale> textareas into one
    {"en": [...], "de": [...], "fr": [...]} field. Stops are matched
    across languages by line position (line 1 of each textarea is the
    same stop), and the icon is always taken from the English line at
    that position when one exists - so admins only need to keep the
    icon consistent in the English textarea, not retype it three times.
    """
    per_locale = {loc: parse_itinerary_textarea(form.get(f"itinerary_{loc}", "")) for loc in SUPPORTED_LOCALES}
    en_stops = per_locale.get(DEFAULT_LOCALE, [])
    result = {}
    for loc, stops in per_locale.items():
        merged = []
        for i, stop in enumerate(stops):
            icon = en_stops[i]["icon"] if i < len(en_stops) and en_stops[i]["icon"] else stop["icon"]
            merged.append({"icon": icon, "title": stop["title"], "description": stop["description"]})
        result[loc] = merged
    return result


def parse_safari_form(form):
    """Build the data dict create_safari()/update_safari() expect from
    a submitted admin form. Returns (data, errors)."""
    errors = []
    data = {
        "accent": form.get("accent", "lagoon"),
        "emoji": form.get("emoji", "").strip(),
    }
    if data["accent"] not in ACCENT_CHOICES:
        data["accent"] = "lagoon"

    try:
        data["display_order"] = int(form.get("display_order", 0))
    except ValueError:
        data["display_order"] = 0

    for field in db.TRANSLATABLE_TEXT_FIELDS:
        data[field] = {loc: form.get(f"{field}_{loc}", "").strip() for loc in SUPPORTED_LOCALES}

    for field in ("overview", "highlights", "included", "excluded", "bring"):
        data[field] = {
            loc: [line.strip() for line in form.get(f"{field}_{loc}", "").splitlines() if line.strip()]
            for loc in SUPPORTED_LOCALES
        }

    data["itinerary"] = build_itinerary_field(form)

    if not data["name"].get(DEFAULT_LOCALE):
        errors.append("Please fill in at least the English name.")

    return data, errors


def save_cover_photo(file, slug):
    """Save an uploaded cover photo as static/covers/<slug>.jpg. Returns
    (success, message) - failure never blocks saving the rest of the
    safari, it just leaves the existing/no cover photo in place."""
    if not file or not file.filename:
        return True, None
    ext = file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""
    if ext not in ("jpg", "jpeg"):
        return False, "Cover photo skipped - please upload a .jpg file."
    os.makedirs(COVERS_DIR, exist_ok=True)
    file.save(os.path.join(COVERS_DIR, f"{slug}.jpg"))
    return True, None


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("is_admin"):
            flash("Please log in to access the admin area.", "error")
            return redirect(url_for("admin_login", next=request.path))
        return view(*args, **kwargs)

    return wrapped


# ---------------------------------------------------------------------------
# Language detection
#
# Automatic, based on the visitor's browser/device language (the standard
# Accept-Language header every browser sends), NOT their IP address. This
# matters for a tourism site in particular: a German visitor's phone is
# still set to German once they land in Kenya, but their IP would just say
# "Kenya", which tells us nothing useful about what language to show. A
# manual switcher (?lang=xx, remembered for the session) always overrides
# the automatic guess.
#
# The admin dashboard is intentionally excluded from all of this and
# always renders in English - see inject_globals() below.
# ---------------------------------------------------------------------------

def get_locale():
    query_lang = request.args.get("lang")
    if query_lang in SUPPORTED_LOCALES:
        session["locale"] = query_lang
        return query_lang
    if session.get("locale") in SUPPORTED_LOCALES:
        return session["locale"]
    best = request.accept_languages.best_match(SUPPORTED_LOCALES)
    locale = best or DEFAULT_LOCALE
    session["locale"] = locale
    return locale


@app.before_request
def load_locale():
    g.locale = get_locale()


def safari_cover_url(slug):
    """Return the cover photo URL for a safari, or None if it hasn't been added yet."""
    path = os.path.join(COVERS_DIR, f"{slug}.jpg")
    if os.path.exists(path):
        return url_for("static", filename=f"covers/{slug}.jpg")
    return None


def localized_contact_info(locale):
    info = dict(CONTACT_INFO)
    info["hours"] = [
        (resolve_locale(h["day"], locale), h["time"]) for h in CONTACT_INFO["hours"]
    ]
    return info


def build_switch_urls():
    """Current page's URL with ?lang=xx swapped for each supported language,
    preserving any other query params (e.g. ?safari=... on the contact page)."""
    urls = {}
    for code in SUPPORTED_LOCALES:
        args = request.args.to_dict(flat=True)
        args["lang"] = code
        urls[code] = request.path + "?" + urlencode(args)
    return urls


@app.context_processor
def inject_globals():
    is_admin_area = request.path.startswith("/admin")
    locale = DEFAULT_LOCALE if is_admin_area else g.locale

    safaris = db.get_all_safaris(locale)
    for s in safaris:
        s["cover_url"] = safari_cover_url(s["slug"])

    return {
        "safaris": safaris,
        "contact": localized_contact_info(locale),
        "current_year": datetime.now().year,
        "tr": lambda key, **kw: translate(key, locale, **kw),
        "locale": locale,
        "SUPPORTED_LOCALES": SUPPORTED_LOCALES,
        "LOCALE_NAMES": LOCALE_NAMES,
        "switch_urls": build_switch_urls(),
    }


# ---------------------------------------------------------------------------
# Public routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    locale = g.locale
    safaris_by_slug = {s["slug"]: s for s in db.get_all_safaris(locale)}

    testimonials = []
    for item in TESTIMONIALS:
        safari = safaris_by_slug.get(item["trip_slug"])
        testimonials.append(
            {
                "quote": resolve_locale(item["quote"], locale),
                "name": item["name"],
                "trip_name": safari["name"] if safari else "",
            }
        )

    faqs = [
        {"q": resolve_locale(item["q"], locale), "a": resolve_locale(item["a"], locale)}
        for item in FAQS
    ]

    return render_template("index.html", testimonials=testimonials, faqs=faqs)


@app.route("/safari/<slug>")
def safari_detail(slug):
    locale = g.locale
    safari = db.get_safari_by_slug(slug, locale)
    if safari is None:
        abort(404)
    safari["cover_url"] = safari_cover_url(safari["slug"])

    others = db.get_other_safaris(slug, locale, limit=3)
    for o in others:
        o["cover_url"] = safari_cover_url(o["slug"])

    return render_template(
        "safari_detail.html", safari=safari, gallery=safari["images"], others=others
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    locale = g.locale
    preselect = request.args.get("safari", "")
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        safari_slug = request.form.get("safari", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash(translate("contact_flash_missing", locale), "error")
            return render_template("contact.html", preselect=safari_slug)

        safari = db.get_safari_by_slug(safari_slug, locale) if safari_slug else None
        db.add_inquiry(
            name=name,
            email=email,
            phone=phone,
            message=message,
            safari_id=safari["id"] if safari else None,
        )

        flash(translate("contact_flash_success", locale), "success")
        return redirect(url_for("contact"))

    return render_template("contact.html", preselect=preselect)


# ---------------------------------------------------------------------------
# Admin routes
#
# Deliberately not translated - only the site's own staff use this area,
# so it always renders in English regardless of visitor locale detection
# (see inject_globals() above, which forces locale="en" for /admin/*).
# ---------------------------------------------------------------------------

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        password = request.form.get("password", "")
        if password == ADMIN_PASSWORD:
            session["is_admin"] = True
            flash("Welcome back.", "success")
            next_url = request.form.get("next") or url_for("admin_dashboard")
            return redirect(next_url)
        flash("Incorrect password.", "error")
    return render_template("admin_login.html", next=request.args.get("next", ""))


@app.route("/admin/logout")
def admin_logout():
    session.pop("is_admin", None)
    flash("You've been logged out.", "success")
    return redirect(url_for("index"))


@app.route("/admin/dashboard")
@login_required
def admin_dashboard():
    inquiries = db.get_all_inquiries(DEFAULT_LOCALE)
    return render_template("admin_dashboard.html", inquiries=inquiries)


@app.route("/admin/upload/<slug>", methods=["POST"])
@login_required
def admin_upload(slug):
    safari = db.get_safari_by_slug(slug, DEFAULT_LOCALE)
    if safari is None:
        abort(404)

    files = request.files.getlist("photos")
    if not files or all(f.filename == "" for f in files):
        flash("No files were selected.", "error")
        return redirect(url_for("admin_dashboard"))

    saved, skipped = 0, 0
    folder = os.path.join(UPLOAD_DIR, slug)
    os.makedirs(folder, exist_ok=True)

    for file in files:
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
            filename = f"{timestamp}_{filename}"
            file.save(os.path.join(folder, filename))
            db.add_gallery_image(safari["id"], filename)
            saved += 1
        elif file and file.filename:
            skipped += 1

    if saved:
        flash(f"Uploaded {saved} photo(s) to {safari['name']}.", "success")
    if skipped:
        flash(f"Skipped {skipped} file(s) with an unsupported format.", "error")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/delete-image/<int:image_id>", methods=["POST"])
@login_required
def admin_delete_image(image_id):
    image = db.get_gallery_image(image_id)
    if image is None:
        abort(404)
    filepath = os.path.join(UPLOAD_DIR, image["safari_slug"], image["filename"])
    if os.path.exists(filepath):
        os.remove(filepath)
    db.delete_gallery_image(image_id)
    flash("Photo deleted.", "success")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/safaris")
@login_required
def admin_safaris():
    safaris = db.get_all_safaris(DEFAULT_LOCALE)
    for s in safaris:
        s["cover_url"] = safari_cover_url(s["slug"])
    return render_template("admin_safaris_list.html", safaris=safaris)


@app.route("/admin/safaris/new", methods=["GET", "POST"])
@login_required
def admin_safari_new():
    if request.method == "POST":
        data, errors = parse_safari_form(request.form)

        base_slug = db.slugify(request.form.get("slug") or data["name"][DEFAULT_LOCALE])
        data["slug"] = db.unique_slug(base_slug)

        if errors:
            for e in errors:
                flash(e, "error")
            return render_template(
                "admin_safari_form.html", form=request.form, is_new=True,
                accent_choices=ACCENT_CHOICES,
            )

        db.create_safari(data)
        ensure_upload_dirs([data["slug"]])

        ok, msg = save_cover_photo(request.files.get("cover_photo"), data["slug"])
        if not ok:
            flash(msg, "error")

        flash(f"Added {data['name'][DEFAULT_LOCALE]}.", "success")
        return redirect(url_for("admin_safaris"))

    form_values = safari_to_form_values(blank_safari_raw())
    return render_template(
        "admin_safari_form.html", form=form_values, is_new=True,
        accent_choices=ACCENT_CHOICES,
    )


@app.route("/admin/safaris/<slug>/edit", methods=["GET", "POST"])
@login_required
def admin_safari_edit(slug):
    raw = db.get_safari_raw(slug)
    if raw is None:
        abort(404)

    if request.method == "POST":
        data, errors = parse_safari_form(request.form)
        data["slug"] = raw["slug"]  # slug is fixed once created - see the form's note

        if errors:
            for e in errors:
                flash(e, "error")
            return render_template(
                "admin_safari_form.html", form=request.form, is_new=False,
                slug=raw["slug"], accent_choices=ACCENT_CHOICES,
                cover_url=safari_cover_url(raw["slug"]),
            )

        db.update_safari(raw["id"], data)

        ok, msg = save_cover_photo(request.files.get("cover_photo"), raw["slug"])
        if not ok:
            flash(msg, "error")

        flash(f"Saved changes to {data['name'][DEFAULT_LOCALE]}.", "success")
        return redirect(url_for("admin_safaris"))

    form_values = safari_to_form_values(raw)
    return render_template(
        "admin_safari_form.html", form=form_values, is_new=False,
        slug=raw["slug"], accent_choices=ACCENT_CHOICES,
        cover_url=safari_cover_url(raw["slug"]),
    )


@app.route("/admin/safaris/<slug>/delete", methods=["POST"])
@login_required
def admin_safari_delete(slug):
    raw = db.get_safari_raw(slug)
    if raw is None:
        abort(404)

    db.delete_safari(raw["id"])

    upload_folder = os.path.join(UPLOAD_DIR, slug)
    if os.path.isdir(upload_folder):
        shutil.rmtree(upload_folder)

    cover_path = os.path.join(COVERS_DIR, f"{slug}.jpg")
    if os.path.exists(cover_path):
        os.remove(cover_path)

    flash(f"Deleted {raw['name'].get(DEFAULT_LOCALE, slug)}.", "success")
    return redirect(url_for("admin_safaris"))


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


# ---------------------------------------------------------------------------
# CLI helper: `flask --app app reset-db` wipes and reseeds the database -
# handy in development, but it permanently deletes all galleries and
# enquiries, so don't run it in production without a backup.
# ---------------------------------------------------------------------------

@app.cli.command("reset-db")
def reset_db_command():
    with app.app_context():
        conn = db.get_db()
        conn.executescript(
            "DROP TABLE IF EXISTS gallery_images;"
            "DROP TABLE IF EXISTS inquiries;"
            "DROP TABLE IF EXISTS safaris;"
        )
        conn.commit()
        db.init_db()
        db.seed_safaris(SEED_SAFARIS)
    print("Database reset and reseeded.")


bootstrap_database()

if __name__ == "__main__":
    app.run(debug=True)

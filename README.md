# Diani Sea Adventures

A Flask website for a sea excursion company on Diani Beach, Kenya, with six
excursion categories, each on its own detail page with a photo gallery you
can manage as an administrator. Automatically shown in English, German or
French depending on the visitor's browser language.

## Features

- Home page with all six excursions, "why choose us", testimonials, and FAQ
- A dedicated page per excursion: full details, quick facts, what's
  included, what to bring, a step-by-step itinerary timeline with icons,
  and a photo gallery
- Cover photo per excursion (`static/covers/<slug>.jpg`) shown on the
  homepage, detail page hero, and related-excursions cards. If a cover
  photo hasn't been added yet, the site falls back to a colored block with
  an emoji instead of a broken image - so it's safe to add a new excursion
  before you have a professional photo of it.
- **Automatic language detection** - the site reads the visitor's browser
  language (the standard `Accept-Language` header every browser sends) and
  shows English, German, or French accordingly, with a manual switcher in
  the nav that overrides the guess and is remembered for the session. See
  "Languages" below for how this works and how to add more.
- Contact page with an enquiry form (saved to the database) and a map
- Password-protected admin dashboard to add, edit, and delete safaris
  (including their itinerary), upload/delete gallery and cover photos, and
  review enquiries - deliberately English-only, since it's for site staff,
  not visitors. See "Managing safaris from the admin panel" below.
- **A real SQLite database** (`data/diani.db`) for excursions, gallery
  photo metadata, and enquiries - built on Python's built-in `sqlite3`
  module, so there's nothing extra to install. Uploaded photo *files*
  still live under `static/uploads/<excursion-slug>/`; the database just
  tracks which photo belongs to which excursion.
- Mobile-first, responsive layout with no heavy front-end frameworks

## Getting started

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Languages

The site ships with English, German and French. Language detection works
like this, in order:

1. If the URL has `?lang=de` (or `en`/`fr`), that language is used and
   remembered for the visitor's session - this is what the nav switcher
   does.
2. Otherwise, if a language was already chosen earlier in the session,
   that's used again.
3. Otherwise, the visitor's browser `Accept-Language` header is matched
   against the supported languages, falling back to English if there's no
   match.

This deliberately does **not** use IP-based geolocation: a tourist's phone
is usually still set to their home language regardless of which country
they're physically in, so the browser's own language setting is a more
reliable signal than "what country does this IP belong to" - and it needs
no external service, API key, or GeoIP database.

**Adding a fourth language:** add a new key (e.g. `"es"`) to every dict in
`i18n.py`'s `UI_STRINGS`, add `"es"` to `SUPPORTED_LOCALES` and give it a
display name in `LOCALE_NAMES`, then add an `"es"` key alongside the
existing `"en"`/`"de"`/`"fr"` entries for every translatable field in each
safari in `data.py` (and in `TESTIMONIALS`/`FAQS`). Existing safaris in an
already-seeded database won't pick up the new language automatically - use
`flask --app app reset-db` to reseed, or add the missing translations to
the database rows directly.

**Admin dashboard is English-only on purpose** - only your own staff use
it, so translating internal tooling wasn't worth the extra maintenance.

## Admin access

Go to the "Admin" link in the footer (or visit `/admin/login`).

- Default password: `diani2026`

**Change this before putting the site online.** Set an environment variable
instead of using the default:

```bash
export ADMIN_PASSWORD="a-strong-password-of-your-choice"
export SECRET_KEY="a-long-random-string"
python app.py
```

On Windows (PowerShell):

```powershell
$env:ADMIN_PASSWORD="a-strong-password-of-your-choice"
$env:SECRET_KEY="a-long-random-string"
python app.py
```

From the admin dashboard you can:
- Upload one or more photos (JPG, PNG, WEBP, GIF) to any safari's gallery
- Delete photos from a gallery
- View enquiries submitted through the contact form
- Go to **Manage safaris** to add, edit, or delete safaris (see below)

## Managing safaris from the admin panel

Go to **Manage safaris** from the admin dashboard nav. From there:

- **Add a new safari** - fills in a form for every field (name, pricing,
  what's included, itinerary, etc.) in English, German, and French. You
  only *have* to fill in the English name; anything left blank in German
  or French falls back to showing the English text on the site until you
  come back and translate it.
- **Edit an existing safari** - same form, pre-filled with the current
  content.
- **Delete a safari** - removes it, its gallery photos, and its cover
  photo permanently. There's a confirmation prompt since this can't be
  undone.
- **Upload a cover photo** - right on the edit form now, as a `.jpg`
  upload. No cover photo yet? The site shows the emoji + accent color
  fallback automatically, same as it always has.

**The URL slug is fixed once a safari is created** - it can't be edited
later. This is deliberate: gallery photo folders and cover photos are
matched to a safari by its slug, and renaming it would silently orphan
them. If you really need to change a safari's URL, delete it and create a
new one (re-uploading its photos), or edit the `slug` column directly in
the database.

**Editing the itinerary:** each language has its own textarea, one stop
per line, formatted as `icon | title | short description`, for example:

```
🏨 | Hotel pick-up | We collect you from your accommodation.
⛵ | Board the boat | Head out to search for dolphins.
```

The **icon only needs to be typed in the English textarea** - the German
and French versions of the same stop (matched by line number) reuse it
automatically, so you don't have to retype an emoji three times. Keep the
same number of lines, in the same order, across all three languages so
they line up correctly; if a translation is well short of the others for
now, that's fine, it just won't have a translated itinerary until you
catch it up.

## The database

Safari details, gallery photo metadata, and contact-form enquiries live in
a SQLite database at `data/diani.db`. It's created automatically the first
time you run the app, and seeded with the six default excursions from
`data.SEED_SAFARIS`.

> **Upgrading from an older version of this project?** Safari text fields
> used to be stored as plain strings; they're now stored as
> `{"en": ..., "de": ..., "fr": ...}` JSON so each field can hold all three
> languages. An existing `data/diani.db` from before this change is **not**
> compatible - run `flask --app app reset-db` to migrate (see the warning
> below: back up first if you've collected real photos or enquiries).

Three tables:

- `safaris` - one row per excursion category
- `gallery_images` - one row per uploaded photo, linked to a safari
  (the actual image file lives on disk under `static/uploads/<slug>/`)
- `inquiries` - contact-form submissions, optionally linked to a safari

**Editing safari content:** the admin panel's **Manage safaris** page (see
above) is the normal way to add, edit, or delete safaris now - no need to
touch `data.py` or the database directly for day-to-day changes.

`data.py`'s `SEED_SAFARIS` only matters before the database exists yet
(the very first run) or if you want to bulk-edit content by hand and
reseed from scratch. Once the database is seeded, editing `data.py` has
no effect on existing safaris until you either edit the database rows
directly (e.g. with the `sqlite3` CLI or
[DB Browser for SQLite](https://sqlbrowser.org/)) or wipe and reseed
everything with:

```bash
flask --app app reset-db
```

**Warning:** `reset-db` permanently deletes every safari, gallery photo
record, and enquiry currently in the database - including anything added
or edited through the admin panel - and replaces them with a fresh copy
of `data.py`'s `SEED_SAFARIS`. It won't delete photo *files* on disk
(you'd clear `static/uploads/` separately for a full reset). Back up
`data/diani.db` first if there's anything in it you'd miss.

`TESTIMONIALS`, `FAQS`, and `CONTACT_INFO` aren't stored in the database
at all, so those three are still edited directly in `data.py`, any time,
and take effect on the next page load with no reseeding needed.

**Note on the Jet Ski Safari:** unlike the other five excursions, this one
wasn't sourced from a real excursions page - it was written from general
knowledge of how jet ski rentals typically run on Diani Beach (short,
tide-dependent, guided sessions through a marked reef channel). The price
and duration are a reasonable placeholder, not confirmed real rates -
double-check and update them (through the admin panel, easiest) before
this goes live. It also doesn't have a cover photo yet - add one through
the edit form whenever you have it; until then the site shows a colored
block with a 🚤 instead.

**Switching to Postgres or MySQL:** the code only touches the database
through the small `db.py` module using raw SQL, written against SQLite. If
you outgrow SQLite (e.g. you need multiple app servers writing to the same
database), you'd swap `db.py`'s `sqlite3` connection for a driver like
`psycopg` and adjust the schema's SQLite-specific syntax (mainly
`AUTOINCREMENT`). For a single-server small-business site, SQLite is
genuinely fine indefinitely.

## Deploying

This app is ready to run behind a production WSGI server such as gunicorn:

```bash
pip install gunicorn
gunicorn app:app
```

Make sure the `static/uploads/` folder is writable by whichever user runs the
app, and that `SECRET_KEY` / `ADMIN_PASSWORD` are set as environment
variables rather than left at their defaults.

## Project structure

```
diani-sea-adventures/
├── app.py                  # Flask routes, locale detection, admin auth, uploads
├── db.py                   # SQLite schema, connection handling, queries
├── data.py                 # Seed content, testimonials, FAQ, contact info (all per-language)
├── i18n.py                 # Supported languages, static UI string translations
├── requirements.txt
├── data/
│   └── diani.db             # Created automatically on first run
├── static/
│   ├── css/style.css
│   ├── js/main.js
│   ├── covers/<slug>.jpg   # Cover photo per safari (add your own; optional)
│   └── uploads/<slug>/     # Gallery photo files, created automatically
└── templates/
    ├── base.html
    ├── index.html
    ├── safari_detail.html
    ├── contact.html
    ├── admin_login.html
    ├── admin_dashboard.html
    ├── admin_safaris_list.html
    ├── admin_safari_form.html
    └── 404.html
```

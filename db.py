"""
Database layer for Diani Sea Adventures, built on Python's built-in
sqlite3 module - a real SQL database with tables, foreign keys and
constraints, but no extra package to install.

Three tables:
- safaris:        the six safari categories and all their content
- gallery_images: one row per uploaded photo, linked to a safari
- inquiries:      contact-form submissions, optionally linked to a safari

Photo files themselves still live on disk under static/uploads/<slug>/ -
only the filename and metadata are stored in the database, which is the
normal pattern for file uploads (databases are for structured data and
lookups, not for storing binary blobs).

Translatable safari fields are stored as JSON-encoded {"en": ..., "de":
..., "fr": ...} dicts (see i18n.py). Every function that returns safari
data takes a `locale` argument and resolves those dicts down to a single
language before handing back a plain dict, so templates and the rest of
the app never have to think about translation - they just see
`safari["name"]` already in the right language.

Rows are returned as plain dicts (not sqlite3.Row objects) so templates
can use the same `safari.name` / `image.filename` dot-access they would
with an ORM.
"""

import json
import re
import sqlite3
from datetime import datetime

from flask import current_app, g

from i18n import DEFAULT_LOCALE, resolve_locale

SCHEMA = """
CREATE TABLE IF NOT EXISTS safaris (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT UNIQUE NOT NULL,
    accent TEXT DEFAULT 'lagoon',
    emoji TEXT DEFAULT '',
    name TEXT NOT NULL,
    tagline TEXT DEFAULT '{}',
    teaser TEXT DEFAULT '{}',
    duration TEXT DEFAULT '{}',
    group_size TEXT DEFAULT '{}',
    price TEXT DEFAULT '{}',
    difficulty TEXT DEFAULT '{}',
    departs TEXT DEFAULT '{}',
    best_time TEXT DEFAULT '{}',
    overview TEXT DEFAULT '{}',
    highlights TEXT DEFAULT '{}',
    included TEXT DEFAULT '{}',
    excluded TEXT DEFAULT '{}',
    bring TEXT DEFAULT '{}',
    itinerary TEXT DEFAULT '{}',
    display_order INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS gallery_images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    safari_id INTEGER NOT NULL REFERENCES safaris(id) ON DELETE CASCADE,
    filename TEXT NOT NULL,
    uploaded_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS inquiries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT DEFAULT '',
    message TEXT NOT NULL,
    safari_id INTEGER REFERENCES safaris(id) ON DELETE SET NULL,
    received_at TEXT NOT NULL
);
"""

# Every one of these is stored as JSON: a dict of {locale: string} for the
# first group, {locale: [strings, ...]} for the second. Only slug, accent,
# emoji and display_order are plain, non-translatable columns.
TRANSLATABLE_TEXT_FIELDS = (
    "name", "tagline", "teaser", "duration", "group_size",
    "price", "difficulty", "departs", "best_time",
)
TRANSLATABLE_LIST_FIELDS = (
    "overview", "highlights", "included", "excluded", "bring", "itinerary",
)
ALL_TRANSLATABLE_FIELDS = TRANSLATABLE_TEXT_FIELDS + TRANSLATABLE_LIST_FIELDS


# ---------------------------------------------------------------------------
# Connection handling
# ---------------------------------------------------------------------------

def get_db():
    """Return a per-request SQLite connection, opening one if needed."""
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE_PATH"])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(exc=None):
    conn = g.pop("db", None)
    if conn is not None:
        conn.close()


def init_app(app):
    app.teardown_appcontext(close_db)


def init_db():
    conn = get_db()
    conn.executescript(SCHEMA)
    _migrate_add_missing_columns(conn)
    conn.commit()


def _migrate_add_missing_columns(conn):
    """
    Lightweight, additive migration: add newly-introduced columns to an
    already-existing safaris table without touching existing data. Safe
    to run on every startup - it's a no-op once the column exists.

    (This only helps if the table already exists in the newer JSON-per-
    locale shape. Upgrading from a much older version of this project,
    from before safari fields were stored as JSON, still needs
    `flask --app app reset-db` - see the README.)
    """
    existing = {row["name"] for row in conn.execute("PRAGMA table_info(safaris)")}
    if "itinerary" not in existing:
        conn.execute("ALTER TABLE safaris ADD COLUMN itinerary TEXT DEFAULT '{}'")


# ---------------------------------------------------------------------------
# Row -> dict helpers
# ---------------------------------------------------------------------------

def _safari_row_to_dict(row, locale=DEFAULT_LOCALE):
    d = dict(row)
    for field in ALL_TRANSLATABLE_FIELDS:
        raw = json.loads(d[field]) if d[field] else {}
        default = [] if field in TRANSLATABLE_LIST_FIELDS else ""
        d[field] = resolve_locale(raw, locale) if raw else default
    d["images"] = get_gallery_images(d["id"])
    return d


def _image_row_to_dict(row):
    return dict(row)


def _inquiry_row_to_dict(row, safaris_by_id):
    d = dict(row)
    d["safari"] = safaris_by_id.get(d["safari_id"])
    return d


# ---------------------------------------------------------------------------
# Safaris
# ---------------------------------------------------------------------------

def get_all_safaris(locale=DEFAULT_LOCALE):
    rows = get_db().execute(
        "SELECT * FROM safaris ORDER BY display_order"
    ).fetchall()
    return [_safari_row_to_dict(r, locale) for r in rows]


def get_safari_by_slug(slug, locale=DEFAULT_LOCALE):
    row = get_db().execute(
        "SELECT * FROM safaris WHERE slug = ?", (slug,)
    ).fetchone()
    return _safari_row_to_dict(row, locale) if row else None


def get_other_safaris(slug, locale=DEFAULT_LOCALE, limit=3):
    rows = get_db().execute(
        "SELECT * FROM safaris WHERE slug != ? ORDER BY display_order LIMIT ?",
        (slug, limit),
    ).fetchall()
    return [_safari_row_to_dict(r, locale) for r in rows]


def count_safaris():
    return get_db().execute("SELECT COUNT(*) FROM safaris").fetchone()[0]


def get_all_slugs():
    rows = get_db().execute("SELECT slug FROM safaris").fetchall()
    return [r["slug"] for r in rows]


def _safari_row_to_raw_dict(row):
    """
    Like _safari_row_to_dict, but WITHOUT resolving translatable fields
    down to one locale - each stays as its full {"en": ..., "de": ...,
    "fr": ...} dict. Used to populate the admin edit form, which needs to
    show and edit all three languages at once.
    """
    d = dict(row)
    for field in ALL_TRANSLATABLE_FIELDS:
        d[field] = json.loads(d[field]) if d[field] else {}
    return d


def get_safari_raw(slug):
    row = get_db().execute(
        "SELECT * FROM safaris WHERE slug = ?", (slug,)
    ).fetchone()
    return _safari_row_to_raw_dict(row) if row else None


def slugify(text):
    """Turn a safari name into a URL-friendly slug, e.g. 'Jet Ski Safari' -> 'jet-ski-safari'."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "safari"


def unique_slug(base_slug, exclude_slug=None):
    """Add -2, -3, etc. if base_slug is already taken by a different safari."""
    existing = set(get_all_slugs())
    existing.discard(exclude_slug)
    if base_slug not in existing:
        return base_slug
    n = 2
    while f"{base_slug}-{n}" in existing:
        n += 1
    return f"{base_slug}-{n}"


def next_display_order():
    row = get_db().execute("SELECT MAX(display_order) FROM safaris").fetchone()
    return (row[0] or 0) + 1


def create_safari(data):
    """
    Create a new safari. `data` is a dict with slug, accent, emoji, and
    every field in ALL_TRANSLATABLE_FIELDS as a {"en": ..., "de": ...,
    "fr": ...} dict (or {"en": [...], ...} for list fields). Returns the
    new safari's slug.
    """
    conn = get_db()
    payload = dict(data)
    for field in ALL_TRANSLATABLE_FIELDS:
        payload[field] = json.dumps(payload.get(field, {}))
    payload["display_order"] = next_display_order()
    columns = ", ".join(payload.keys())
    placeholders = ", ".join("?" for _ in payload)
    conn.execute(
        f"INSERT INTO safaris ({columns}) VALUES ({placeholders})",
        tuple(payload.values()),
    )
    conn.commit()
    return payload["slug"]


def update_safari(safari_id, data):
    """
    Update an existing safari (by id, since slug is immutable after
    creation - see the admin form). `data` has the same shape as
    create_safari's.
    """
    conn = get_db()
    payload = dict(data)
    for field in ALL_TRANSLATABLE_FIELDS:
        payload[field] = json.dumps(payload.get(field, {}))
    set_clause = ", ".join(f"{col} = ?" for col in payload.keys())
    conn.execute(
        f"UPDATE safaris SET {set_clause} WHERE id = ?",
        tuple(payload.values()) + (safari_id,),
    )
    conn.commit()


def delete_safari(safari_id):
    """Delete a safari and its gallery image rows (cascades via FK).
    Does NOT touch files on disk - the caller (app.py) handles removing
    the uploads folder and cover photo, since that's a filesystem
    concern, not a database one."""
    conn = get_db()
    conn.execute("DELETE FROM safaris WHERE id = ?", (safari_id,))
    conn.commit()


def seed_safaris(seed_list):
    conn = get_db()
    for order, entry in enumerate(seed_list):
        payload = dict(entry)
        for field in ALL_TRANSLATABLE_FIELDS:
            payload[field] = json.dumps(payload.get(field, {}))
        payload["display_order"] = order
        columns = ", ".join(payload.keys())
        placeholders = ", ".join("?" for _ in payload)
        conn.execute(
            f"INSERT INTO safaris ({columns}) VALUES ({placeholders})",
            tuple(payload.values()),
        )
    conn.commit()


# ---------------------------------------------------------------------------
# Gallery images
# ---------------------------------------------------------------------------

def get_gallery_images(safari_id):
    rows = get_db().execute(
        "SELECT * FROM gallery_images WHERE safari_id = ? ORDER BY uploaded_at DESC",
        (safari_id,),
    ).fetchall()
    return [_image_row_to_dict(r) for r in rows]


def add_gallery_image(safari_id, filename):
    conn = get_db()
    conn.execute(
        "INSERT INTO gallery_images (safari_id, filename, uploaded_at) VALUES (?, ?, ?)",
        (safari_id, filename, datetime.utcnow().isoformat()),
    )
    conn.commit()


def get_gallery_image(image_id):
    row = get_db().execute(
        "SELECT gi.*, s.slug AS safari_slug FROM gallery_images gi "
        "JOIN safaris s ON s.id = gi.safari_id WHERE gi.id = ?",
        (image_id,),
    ).fetchone()
    return dict(row) if row else None


def delete_gallery_image(image_id):
    conn = get_db()
    conn.execute("DELETE FROM gallery_images WHERE id = ?", (image_id,))
    conn.commit()


# ---------------------------------------------------------------------------
# Inquiries
# ---------------------------------------------------------------------------

def add_inquiry(name, email, phone, message, safari_id):
    conn = get_db()
    conn.execute(
        "INSERT INTO inquiries (name, email, phone, message, safari_id, received_at) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (name, email, phone, message, safari_id, datetime.utcnow().isoformat()),
    )
    conn.commit()


def get_all_inquiries(locale=DEFAULT_LOCALE):
    rows = get_db().execute(
        "SELECT * FROM inquiries ORDER BY received_at DESC"
    ).fetchall()
    safaris_by_id = {s["id"]: s for s in get_all_safaris(locale)}
    return [_inquiry_row_to_dict(r, safaris_by_id) for r in rows]

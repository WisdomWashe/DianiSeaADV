"""
Lightweight internationalisation for Diani Sea Adventures.

No extra dependency (no Flask-Babel) - just plain Python dicts. There are
two kinds of translatable content in this app:

1. Static UI strings (buttons, headings, labels) - defined in UI_STRINGS
   below and looked up with translate(key, locale).
2. Dynamic content stored in the database (safari names, descriptions,
   testimonials, FAQs) - stored as {"en": ..., "de": ..., "fr": ...} dicts
   and resolved with resolve_locale(value, locale).

The admin dashboard is deliberately NOT translated - it's only used by the
site's own staff, so keeping it in one language keeps this file smaller
and avoids translating internal tooling nobody but the owner sees.
"""

SUPPORTED_LOCALES = ["en", "de", "fr"]
DEFAULT_LOCALE = "en"

LOCALE_NAMES = {
    "en": "English",
    "de": "Deutsch",
    "fr": "Français",
}


def resolve_locale(value, locale):
    """
    Resolve a {"en": ..., "de": ..., "fr": ...} dict down to a single
    value for `locale`, falling back to English if that language's
    content is missing OR blank (e.g. an admin saved a new safari but
    hasn't filled in the German/French fields yet), and finally to
    whatever's available rather than showing nothing.
    """
    if not isinstance(value, dict):
        return value
    if value.get(locale):
        return value[locale]
    if value.get(DEFAULT_LOCALE):
        return value[DEFAULT_LOCALE]
    return next((v for v in value.values() if v), "")


def translate(key, locale, **kwargs):
    """Look up a static UI string, falling back to English, then the key itself."""
    text = UI_STRINGS.get(locale, {}).get(key)
    if text is None:
        text = UI_STRINGS.get(DEFAULT_LOCALE, {}).get(key, key)
    if kwargs:
        try:
            return text.format(**kwargs)
        except (KeyError, IndexError):
            return text
    return text


# ---------------------------------------------------------------------------
# Static UI strings
#
# NOTE: a couple of these (hero_title_html, intro_feature*_title) contain
# hard-coded HTML (<em>, &amp;) and are rendered with the |safe filter in
# templates. They're all written by us, not user input, so that's safe.
#
# NOTE: hero_title_html says "Six" - if you add a 7th safari, update the
# wording in all three languages below (the safari *count* elsewhere on
# the homepage is computed automatically from the database).
# ---------------------------------------------------------------------------

UI_STRINGS = {
    "en": {
        "nav_safaris": "Safaris",
        "nav_about": "About",
        "nav_faq": "FAQ",
        "nav_contact": "Contact",

        "hero_eyebrow": "Diani Beach, Kwale County",
        "hero_title_html": "Six ways to get out on the <em>Indian Ocean</em>",
        "hero_subtitle": (
            "From early-morning dolphin trips to a quick jet ski ride, our "
            "crews know this stretch of coast well. Small groups, "
            "experienced guides, and most trips depart right from Diani "
            "Beach."
        ),
        "hero_cta_browse": "Browse safaris",
        "hero_cta_ask": "Ask us a question",
        "hero_stat_safaris_label": "Signature safaris",
        "hero_stat_years_label": "Years on this coast",

        "intro_heading": "Local crews, small groups, honest weather calls",
        "intro_body": (
            "We're based right on Diani Beach, not booked through a call "
            "centre elsewhere. Every excursion on this site is run by the "
            "same crews we'd put our own families on: boats that are well "
            "maintained, captains who know the channel by feel, and a "
            "policy of rescheduling rather than pushing a trip out in bad "
            "weather."
        ),
        "intro_feature1_title": "Licensed &amp; insured boats",
        "intro_feature1_body": "Every vessel is registered with the Kenya Maritime Authority and carries full safety equipment.",
        "intro_feature2_title": "Small group sizes",
        "intro_feature2_body": "We cap numbers per boat so the wildlife isn't crowded and you're not queuing for a mask.",
        "intro_feature3_title": "Free hotel transfers",
        "intro_feature3_body": "Pick-up and drop-off along Diani Beach Road is included with every excursion.",

        "safaris_heading": "Choose your safari",
        "safaris_subheading": "Each trip runs on its own schedule and boat - pick the one that matches how you want to spend the day.",
        "safari_row_view_details": "View safari details",

        "testimonials_heading": "What guests say",
        "testimonials_subheading": "A few notes from people who've been out with us this season.",

        "faq_heading": "Good to know before you book",
        "faq_subheading": "The questions we're asked most often. Anything else, just get in touch.",

        "cta_heading": "Ready to get out on the water?",
        "cta_subheading": "Tell us your dates and we'll help you pick the right safari.",
        "cta_button": "Get in touch",

        "footer_blurb": "Sea excursions from Diani Beach: dolphin trips, coral reefs, deep-sea fishing, canoe rides and jet ski adventures.",
        "footer_explore_heading": "Explore",
        "footer_all_safaris": "All safaris",
        "footer_about_us": "About us",
        "footer_faq": "FAQ",
        "footer_contact": "Contact",
        "footer_safaris_heading": "Safaris",
        "footer_contact_heading": "Get in touch",
        "footer_rights": "© {year} Diani Sea Adventures. All rights reserved.",
        "footer_admin": "Admin",

        "detail_breadcrumb_home": "Home",
        "detail_breadcrumb_safaris": "Safaris",
        "detail_fact_duration": "Duration",
        "detail_fact_group_size": "Group size",
        "detail_fact_price": "Price",
        "detail_fact_level": "Level",
        "detail_fact_departs": "Departs",
        "detail_overview_heading": "Overview",
        "detail_highlights_heading": "Highlights",
        "detail_included_heading": "What's included",
        "detail_included_label": "Included",
        "detail_excluded_label": "Not included",
        "detail_bring_heading": "What to bring",
        "detail_best_time_heading": "Best time to go",
        "detail_enquire_button": "Enquire about this safari",
        "detail_call_whatsapp": "Prefer to talk first? Call or WhatsApp",
        "detail_gallery_heading": "Gallery",
        "detail_gallery_caption": "Photos from recent {name} trips.",
        "detail_gallery_empty": "Photos coming soon - check back after our next {name}.",
        "detail_itinerary_heading": "How the day unfolds",
        "detail_related_heading": "Other safaris",

        "contact_page_title": "Let's find you a safari",
        "contact_page_subtitle": "Send us your dates and how many people are travelling, and we'll reply with availability - usually within a few hours.",
        "contact_label_name": "Full name",
        "contact_label_email": "Email",
        "contact_label_phone": "Phone / WhatsApp (optional)",
        "contact_label_safari": "Which safari?",
        "contact_option_not_sure": "Not sure yet",
        "contact_label_message": "Your message",
        "contact_message_placeholder": "Dates, number of guests, hotel name, or any questions.",
        "contact_button_send": "Send enquiry",
        "contact_card_heading": "Contact details",
        "contact_dt_phone": "Phone / WhatsApp",
        "contact_dt_email": "Email",
        "contact_dt_location": "Location",
        "contact_dt_hours": "Opening hours",
        "contact_flash_missing": "Please fill in your name, email and message.",
        "contact_flash_success": "Thanks! Your enquiry has been sent - we'll reply within 24 hours.",

        "notfound_heading": "🧭 Lost at sea",
        "notfound_message": "We couldn't find that page. It may have moved, or the link's out of date.",
        "notfound_button": "Back to safaris",

        "meta_default_description": "Dolphin trips, snorkeling, deep-sea fishing, canoe excursions and jet ski rides from Diani Beach, Kenya.",
        "contact_meta_description": "Get in touch to book a sea excursion from Diani Beach - dolphin trips, snorkeling, fishing, canoe trips and jet ski rides.",
    },
    "de": {
        "nav_safaris": "Safaris",
        "nav_about": "Über uns",
        "nav_faq": "FAQ",
        "nav_contact": "Kontakt",

        "hero_eyebrow": "Diani Beach, Kwale County",
        "hero_title_html": "Sechs Wege, den <em>Indischen Ozean</em> zu erkunden",
        "hero_subtitle": (
            "Von frühmorgendlichen Delfintouren bis zur schnellen "
            "Jetski-Fahrt - unsere Crews kennen diesen Küstenabschnitt gut. "
            "Kleine Gruppen, erfahrene Guides, und die meisten Touren "
            "starten direkt am Diani Beach."
        ),
        "hero_cta_browse": "Safaris ansehen",
        "hero_cta_ask": "Frage stellen",
        "hero_stat_safaris_label": "Signature-Safaris",
        "hero_stat_years_label": "Jahre an dieser Küste",

        "intro_heading": "Lokale Crews, kleine Gruppen, ehrliche Wetterentscheidungen",
        "intro_body": (
            "Wir sind direkt am Diani Beach ansässig, nicht über ein "
            "Callcenter irgendwo anders erreichbar. Jeder Ausflug auf "
            "dieser Website wird von denselben Crews durchgeführt, denen "
            "wir auch unsere eigenen Familien anvertrauen würden: gut "
            "gewartete Boote, Kapitäne, die den Kanal aus dem Effeff "
            "kennen, und die Politik, eine Tour bei schlechtem Wetter "
            "lieber zu verschieben als durchzuziehen."
        ),
        "intro_feature1_title": "Lizenzierte &amp; versicherte Boote",
        "intro_feature1_body": "Jedes Boot ist bei der Kenya Maritime Authority registriert und mit vollständiger Sicherheitsausrüstung ausgestattet.",
        "intro_feature2_title": "Kleine Gruppengrößen",
        "intro_feature2_body": "Wir begrenzen die Personenzahl pro Boot, damit die Tierwelt nicht gestört wird und Sie nicht auf eine Maske warten müssen.",
        "intro_feature3_title": "Kostenloser Hoteltransfer",
        "intro_feature3_body": "Abholung und Rücktransfer entlang der Diani Beach Road sind bei jedem Ausflug inbegriffen.",

        "safaris_heading": "Wählen Sie Ihre Safari",
        "safaris_subheading": "Jede Tour hat ihren eigenen Zeitplan und ihr eigenes Boot - wählen Sie die, die zu Ihrem Tag passt.",
        "safari_row_view_details": "Safari-Details ansehen",

        "testimonials_heading": "Was Gäste sagen",
        "testimonials_subheading": "Ein paar Rückmeldungen von Gästen, die diese Saison mit uns unterwegs waren.",

        "faq_heading": "Gut zu wissen, bevor Sie buchen",
        "faq_subheading": "Die Fragen, die uns am häufigsten gestellt werden. Bei allem anderen einfach melden.",

        "cta_heading": "Bereit, aufs Wasser zu kommen?",
        "cta_subheading": "Nennen Sie uns Ihre Reisedaten, wir helfen Ihnen bei der Auswahl der richtigen Safari.",
        "cta_button": "Kontakt aufnehmen",

        "footer_blurb": "Meeresausflüge ab Diani Beach: Delfintouren, Korallenriffe, Hochseeangeln, Kanufahrten und Jetski-Abenteuer.",
        "footer_explore_heading": "Entdecken",
        "footer_all_safaris": "Alle Safaris",
        "footer_about_us": "Über uns",
        "footer_faq": "FAQ",
        "footer_contact": "Kontakt",
        "footer_safaris_heading": "Safaris",
        "footer_contact_heading": "Kontakt aufnehmen",
        "footer_rights": "© {year} Diani Sea Adventures. Alle Rechte vorbehalten.",
        "footer_admin": "Admin",

        "detail_breadcrumb_home": "Startseite",
        "detail_breadcrumb_safaris": "Safaris",
        "detail_fact_duration": "Dauer",
        "detail_fact_group_size": "Gruppengröße",
        "detail_fact_price": "Preis",
        "detail_fact_level": "Niveau",
        "detail_fact_departs": "Abfahrt",
        "detail_overview_heading": "Überblick",
        "detail_highlights_heading": "Highlights",
        "detail_included_heading": "Leistungen",
        "detail_included_label": "Inklusive",
        "detail_excluded_label": "Nicht inklusive",
        "detail_bring_heading": "Was Sie mitbringen sollten",
        "detail_best_time_heading": "Beste Reisezeit",
        "detail_enquire_button": "Diese Safari anfragen",
        "detail_call_whatsapp": "Lieber erst sprechen? Rufen Sie an oder schreiben Sie per WhatsApp",
        "detail_gallery_heading": "Galerie",
        "detail_gallery_caption": "Fotos von aktuellen {name}-Touren.",
        "detail_gallery_empty": "Fotos folgen in Kürze - schauen Sie nach unserer nächsten Tour wieder vorbei.",
        "detail_itinerary_heading": "So läuft der Tag ab",
        "detail_related_heading": "Weitere Safaris",

        "contact_page_title": "Lassen Sie uns die passende Safari für Sie finden",
        "contact_page_subtitle": "Teilen Sie uns Ihre Reisedaten und die Anzahl der Personen mit - wir melden uns meist innerhalb weniger Stunden mit der Verfügbarkeit.",
        "contact_label_name": "Vollständiger Name",
        "contact_label_email": "E-Mail",
        "contact_label_phone": "Telefon / WhatsApp (optional)",
        "contact_label_safari": "Welche Safari?",
        "contact_option_not_sure": "Noch unsicher",
        "contact_label_message": "Ihre Nachricht",
        "contact_message_placeholder": "Reisedaten, Anzahl der Gäste, Hotelname oder weitere Fragen.",
        "contact_button_send": "Anfrage senden",
        "contact_card_heading": "Kontaktdaten",
        "contact_dt_phone": "Telefon / WhatsApp",
        "contact_dt_email": "E-Mail",
        "contact_dt_location": "Standort",
        "contact_dt_hours": "Öffnungszeiten",
        "contact_flash_missing": "Bitte geben Sie Ihren Namen, Ihre E-Mail-Adresse und eine Nachricht ein.",
        "contact_flash_success": "Danke! Ihre Anfrage wurde gesendet - wir antworten innerhalb von 24 Stunden.",

        "notfound_heading": "🧭 Auf See verloren",
        "notfound_message": "Diese Seite konnten wir nicht finden. Möglicherweise wurde sie verschoben, oder der Link ist veraltet.",
        "notfound_button": "Zurück zu den Safaris",

        "meta_default_description": "Delfintouren, Schnorcheln, Hochseeangeln, Kanuausflüge und Jetski-Fahrten ab Diani Beach, Kenia.",
        "contact_meta_description": "Kontaktieren Sie uns, um einen Meeresausflug ab Diani Beach zu buchen - Delfintouren, Schnorcheln, Angeln, Kanufahrten und Jetski-Fahrten.",
    },
    "fr": {
        "nav_safaris": "Safaris",
        "nav_about": "À propos",
        "nav_faq": "FAQ",
        "nav_contact": "Contact",

        "hero_eyebrow": "Diani Beach, comté de Kwale",
        "hero_title_html": "Six façons de découvrir l'<em>océan Indien</em>",
        "hero_subtitle": (
            "Des sorties matinales à la recherche de dauphins à une balade "
            "rapide en jet-ski, nos équipes connaissent bien cette côte. "
            "Petits groupes, guides expérimentés, et la plupart des "
            "excursions partent directement de Diani Beach."
        ),
        "hero_cta_browse": "Voir les safaris",
        "hero_cta_ask": "Poser une question",
        "hero_stat_safaris_label": "Safaris emblématiques",
        "hero_stat_years_label": "Années sur cette côte",

        "intro_heading": "Équipes locales, petits groupes, décisions météo honnêtes",
        "intro_body": (
            "Nous sommes basés directement à Diani Beach, et non "
            "joignables via un centre d'appel ailleurs. Chaque excursion "
            "sur ce site est assurée par les mêmes équipes auxquelles "
            "nous confierions nos propres familles : des bateaux bien "
            "entretenus, des capitaines qui connaissent le chenal comme "
            "leur poche, et une politique consistant à reporter une "
            "sortie plutôt que de la maintenir par mauvais temps."
        ),
        "intro_feature1_title": "Bateaux agréés et assurés",
        "intro_feature1_body": "Chaque bateau est enregistré auprès de la Kenya Maritime Authority et dispose de tout l'équipement de sécurité requis.",
        "intro_feature2_title": "Petits groupes",
        "intro_feature2_body": "Nous limitons le nombre de personnes par bateau afin de ne pas déranger la faune et d'éviter les files d'attente pour un masque.",
        "intro_feature3_title": "Transferts hôtel gratuits",
        "intro_feature3_body": "La prise en charge et le retour le long de Diani Beach Road sont inclus pour chaque excursion.",

        "safaris_heading": "Choisissez votre safari",
        "safaris_subheading": "Chaque excursion a son propre horaire et son propre bateau - choisissez celle qui correspond à la journée que vous souhaitez passer.",
        "safari_row_view_details": "Voir les détails du safari",

        "testimonials_heading": "Ce qu'en disent nos clients",
        "testimonials_subheading": "Quelques retours de clients partis avec nous cette saison.",

        "faq_heading": "Bon à savoir avant de réserver",
        "faq_subheading": "Les questions qu'on nous pose le plus souvent. Pour toute autre question, contactez-nous.",

        "cta_heading": "Prêt à prendre le large ?",
        "cta_subheading": "Indiquez-nous vos dates, nous vous aiderons à choisir le bon safari.",
        "cta_button": "Nous contacter",

        "footer_blurb": "Excursions en mer depuis Diani Beach : sorties dauphins, récifs coralliens, pêche sportive, balades en pirogue et aventures en jet-ski.",
        "footer_explore_heading": "Découvrir",
        "footer_all_safaris": "Tous les safaris",
        "footer_about_us": "À propos",
        "footer_faq": "FAQ",
        "footer_contact": "Contact",
        "footer_safaris_heading": "Safaris",
        "footer_contact_heading": "Nous contacter",
        "footer_rights": "© {year} Diani Sea Adventures. Tous droits réservés.",
        "footer_admin": "Admin",

        "detail_breadcrumb_home": "Accueil",
        "detail_breadcrumb_safaris": "Safaris",
        "detail_fact_duration": "Durée",
        "detail_fact_group_size": "Taille du groupe",
        "detail_fact_price": "Prix",
        "detail_fact_level": "Niveau",
        "detail_fact_departs": "Départ",
        "detail_overview_heading": "Aperçu",
        "detail_highlights_heading": "Points forts",
        "detail_included_heading": "Ce qui est inclus",
        "detail_included_label": "Inclus",
        "detail_excluded_label": "Non inclus",
        "detail_bring_heading": "Quoi apporter",
        "detail_best_time_heading": "Meilleure période",
        "detail_enquire_button": "Demander des informations sur ce safari",
        "detail_call_whatsapp": "Vous préférez en parler d'abord ? Appelez ou écrivez sur WhatsApp",
        "detail_gallery_heading": "Galerie",
        "detail_gallery_caption": "Photos de récentes sorties {name}.",
        "detail_gallery_empty": "Photos bientôt disponibles - repassez après notre prochaine sortie.",
        "detail_itinerary_heading": "Le déroulé de la journée",
        "detail_related_heading": "Autres safaris",

        "contact_page_title": "Trouvons le safari qu'il vous faut",
        "contact_page_subtitle": "Indiquez-nous vos dates et le nombre de personnes, nous vous répondrons avec les disponibilités - généralement sous quelques heures.",
        "contact_label_name": "Nom complet",
        "contact_label_email": "E-mail",
        "contact_label_phone": "Téléphone / WhatsApp (facultatif)",
        "contact_label_safari": "Quel safari ?",
        "contact_option_not_sure": "Pas encore sûr",
        "contact_label_message": "Votre message",
        "contact_message_placeholder": "Dates, nombre de personnes, nom de l'hôtel, ou toute autre question.",
        "contact_button_send": "Envoyer la demande",
        "contact_card_heading": "Coordonnées",
        "contact_dt_phone": "Téléphone / WhatsApp",
        "contact_dt_email": "E-mail",
        "contact_dt_location": "Adresse",
        "contact_dt_hours": "Horaires d'ouverture",
        "contact_flash_missing": "Merci de renseigner votre nom, votre e-mail et un message.",
        "contact_flash_success": "Merci ! Votre demande a été envoyée - nous répondrons sous 24 heures.",

        "notfound_heading": "🧭 Perdu en mer",
        "notfound_message": "Nous n'avons pas trouvé cette page. Elle a peut-être été déplacée, ou le lien n'est plus valide.",
        "notfound_button": "Retour aux safaris",

        "meta_default_description": "Sorties dauphins, plongée avec tuba, pêche sportive, excursions en pirogue et balades en jet-ski depuis Diani Beach, Kenya.",
        "contact_meta_description": "Contactez-nous pour réserver une excursion en mer depuis Diani Beach - sorties dauphins, plongée avec tuba, pêche, balades en pirogue et jet-ski.",
    },
}

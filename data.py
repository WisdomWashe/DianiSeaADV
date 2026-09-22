"""
Content for Diani Sea Adventures.

Safaris now live in the database (see db.py) - the SEED_SAFARIS list
below is only used once, the first time the app runs, to populate that
database. Editing this list after the database already has data has no
effect; edit safaris through the database (or the admin dashboard, if you
add editing there) instead. If you've already run the app before, run
`flask --app app reset-db` to wipe and reseed with any changes made here
(this deletes existing gallery photos and enquiries from the database,
so back it up first if you need to).

Every visitor-facing text field below is a dict keyed by language code
("en", "de", "fr") - see i18n.py for how these get resolved to a single
string for the visitor's detected language. Fields that are lists of
strings (highlights, overview, included, excluded, bring) are the same
shape, just with a list as each language's value instead of a string.

Testimonials reference a safari by "trip_slug" rather than repeating its
name, so the correct translated name is looked up at render time instead
of being duplicated (and risking going out of sync) here.

FAQ answers that mention a safari by name spell it out directly in each
language, since they're full sentences rather than a simple lookup - if
you rename a safari, double check the FAQ text below still matches.
"""

SEED_SAFARIS = [
    {
        "slug": "wasini-island-safari",
        "accent": "lagoon",
        "emoji": "\U0001F42C",
        "name": {
            "en": "Wasini Island Day Trip",
            "de": "Tagesausflug Wasini Island",
            "fr": "Excursion d'une journée à l'île de Wasini",
        },
        "tagline": {
            "en": "Dolphins, snorkeling and a seafood lunch on Wasini Island",
            "de": "Delfine, Schnorcheln und ein Fischmenü auf Wasini Island",
            "fr": "Dauphins, plongée avec tuba et déjeuner de fruits de mer sur l'île de Wasini",
        },
        "teaser": {
            "en": "A full day from the mainland to Wasini Island: dolphin spotting by sailboat, snorkeling over a protected reef, a sandbank stop, and a seafood lunch.",
            "de": "Ein ganzer Tag vom Festland zur Insel Wasini: Delfinbeobachtung per Segelboot, Schnorcheln über einem geschützten Riff, ein Stopp auf einer Sandbank und ein Fischmenü zum Mittagessen.",
            "fr": "Une journée complète depuis le continent jusqu'à l'île de Wasini : observation des dauphins en voilier, plongée avec tuba sur un récif protégé, arrêt sur un banc de sable et déjeuner de fruits de mer.",
        },
        "duration": {
            "en": "Full day (approx. 9-10 hours)",
            "de": "Ganztägig (ca. 9-10 Stunden)",
            "fr": "Journée complète (environ 9 à 10 heures)",
        },
        "group_size": {
            "en": "Shared group tour",
            "de": "Gemeinsame Gruppentour",
            "fr": "Excursion en groupe partagé",
        },
        "price": {
            "en": "€120 per person",
            "de": "120 € pro Person",
            "fr": "120 € par personne",
        },
        "difficulty": {
            "en": "Easy - suitable for all ages",
            "de": "Einfach - für alle Altersgruppen geeignet",
            "fr": "Facile - convient à tous les âges",
        },
        "departs": {
            "en": "Pick-up approx. 5:30am (north coast) / 7:30am (south coast)",
            "de": "Abholung ca. 5:30 Uhr (Nordküste) / 7:30 Uhr (Südküste)",
            "fr": "Prise en charge vers 5h30 (côte nord) / 7h30 (côte sud)",
        },
        "best_time": {
            "en": "Year-round",
            "de": "Ganzjährig",
            "fr": "Toute l'année",
        },
        "highlights": {
            "en": [
                "Dolphin spotting in the Wasini Channel by sailboat",
                "Snorkeling in one of the world's largest protected marine areas",
                "A sandbank stop at low tide",
                "Seafood lunch included (fish, chicken, crab, seasonal fruit)",
                "Optional village walk after lunch",
            ],
            "de": [
                "Delfinbeobachtung im Wasini-Kanal per Segelboot",
                "Schnorcheln in einem der größten Meeresschutzgebiete der Welt",
                "Stopp auf einer Sandbank bei Ebbe",
                "Fischmenü inklusive (Fisch, Hähnchen, Krabbe, Saisonobst)",
                "Optionaler Dorfspaziergang nach dem Mittagessen",
            ],
            "fr": [
                "Observation des dauphins en voilier dans le chenal de Wasini",
                "Plongée avec tuba dans l'une des plus grandes aires marines protégées au monde",
                "Arrêt sur un banc de sable à marée basse",
                "Déjeuner de fruits de mer inclus (poisson, poulet, crabe, fruits de saison)",
                "Promenade optionnelle dans le village après le déjeuner",
            ],
        },
        "overview": {
            "en": [
                "We collect you from your accommodation and drive around an hour "
                "and a half to Shimoni, the gateway to Wasini Island. From there "
                "we board a sailboat and set off to find the resident dolphins - "
                "the boat stops as soon as we spot them, so you can watch, and "
                "sometimes swim with them, up close.",
                "After the dolphin search, we snorkel over Wasini's reef, part of "
                "the third-largest marine protected area in the world, then head "
                "to a sandbank that only appears at low tide to relax before "
                "lunch. A full seafood lunch - fish, chicken, crab and seasonal "
                "fruit with rice, coconut sauce and sea vegetables - is served at "
                "a local restaurant, with an optional village walk afterwards for "
                "anyone who'd like to explore.",
            ],
            "de": [
                "Wir holen Sie in Ihrer Unterkunft ab und fahren rund anderthalb "
                "Stunden nach Shimoni, dem Tor zur Insel Wasini. Von dort geht es "
                "mit dem Segelboot auf die Suche nach den ansässigen Delfinen - "
                "sobald wir sie entdecken, stoppt das Boot, sodass Sie sie aus "
                "nächster Nähe beobachten und manchmal sogar mit ihnen schwimmen "
                "können.",
                "Nach der Delfinsuche schnorcheln wir über dem Riff von Wasini, "
                "das zu einem der drei größten Meeresschutzgebiete der Welt "
                "gehört, und legen dann einen Stopp auf einer Sandbank ein, die "
                "nur bei Ebbe zum Vorschein kommt, bevor es zum Mittagessen "
                "geht. Ein vollständiges Fischmenü - Fisch, Hähnchen, Krabbe und "
                "Saisonobst mit Reis, Kokossoße und Meeresgemüse - wird in einem "
                "lokalen Restaurant serviert, anschließend besteht die "
                "Möglichkeit zu einem optionalen Dorfspaziergang.",
            ],
            "fr": [
                "Nous venons vous chercher à votre hébergement et roulons "
                "environ une heure et demie jusqu'à Shimoni, la porte d'entrée "
                "de l'île de Wasini. De là, nous embarquons sur un voilier à la "
                "recherche des dauphins résidents - dès que nous les repérons, "
                "le bateau s'arrête pour vous permettre de les observer de "
                "près, et parfois même de nager avec eux.",
                "Après la recherche des dauphins, nous plongeons avec tuba "
                "au-dessus du récif de Wasini, qui fait partie de la troisième "
                "plus grande aire marine protégée au monde, puis nous nous "
                "arrêtons sur un banc de sable qui n'apparaît qu'à marée basse "
                "pour nous détendre avant le déjeuner. Un déjeuner complet de "
                "fruits de mer - poisson, poulet, crabe et fruits de saison "
                "avec riz, sauce à la noix de coco et légumes de mer - est "
                "servi dans un restaurant local, avec une promenade optionnelle "
                "dans le village pour ceux qui souhaitent explorer.",
            ],
        },
        "included": {
            "en": [
                "Hotel transfers",
                "Parking fees",
                "Boat trip",
                "Snorkeling equipment and life jackets",
                "Snorkeling guide, including personal support for non-swimmers",
                "Lunch",
            ],
            "de": [
                "Transfer von und zur Unterkunft",
                "Parkgebühren",
                "Bootsfahrt",
                "Schnorchelausrüstung und Schwimmwesten",
                "Schnorchelguide, inklusive persönlicher Unterstützung für Nichtschwimmer",
                "Mittagessen",
            ],
            "fr": [
                "Transferts depuis et vers l'hébergement",
                "Frais de parking",
                "Sortie en bateau",
                "Équipement de plongée avec tuba et gilets de sauvetage",
                "Guide de plongée, avec accompagnement personnalisé pour les non-nageurs",
                "Déjeuner",
            ],
        },
        "excluded": {
            "en": [
                "Diving (available on request, extra charge)",
                "Visit to the Shimoni caves (extra charge)",
                "Private boat tour (on request, extra cost)",
                "Deluxe seafood platter upgrade (lobster, calamari, octopus)",
                "Drinks",
                "Tips for drivers, guides and other staff",
            ],
            "de": [
                "Tauchen (auf Anfrage, gegen Aufpreis)",
                "Besuch der Shimoni-Höhlen (gegen Aufpreis)",
                "Private Bootstour (auf Anfrage, gegen Aufpreis)",
                "Upgrade auf Deluxe-Fischplatte (Languste, Tintenfisch, Oktopus)",
                "Getränke",
                "Trinkgeld für Fahrer, Guides und weiteres Personal",
            ],
            "fr": [
                "Plongée sous-marine (sur demande, supplément)",
                "Visite des grottes de Shimoni (supplément)",
                "Excursion privée en bateau (sur demande, supplément)",
                "Supplément plateau de fruits de mer deluxe (langouste, calamars, poulpe)",
                "Boissons",
                "Pourboires pour les chauffeurs, guides et autre personnel",
            ],
        },
        "bring": {
            "en": [
                "Swimwear and a light cover-up",
                "Reef-safe sunscreen",
                "A hat, sunglasses and a towel",
                "Cash for optional extras and tips",
            ],
            "de": [
                "Badebekleidung und einen leichten Überwurf",
                "Riffverträglichen Sonnenschutz",
                "Hut, Sonnenbrille und Handtuch",
                "Bargeld für optionale Extras und Trinkgeld",
            ],
            "fr": [
                "Maillot de bain et une tenue légère",
                "Crème solaire respectueuse des récifs",
                "Un chapeau, des lunettes de soleil et une serviette",
                "De l'argent liquide pour les extras et les pourboires",
            ],
        },
        "itinerary": {
            "en": [
                {"icon": "\U0001F3E8", "title": "Pick-up & drive to Shimoni", "description": "We collect you from your accommodation and drive about 90 minutes to Shimoni."},
                {"icon": "\u26F5", "title": "Board the sailboat", "description": "Head out into the Wasini Channel to search for dolphins."},
                {"icon": "\U0001F42C", "title": "Dolphin watching", "description": "The boat slows down and follows at a respectful distance once a pod is found."},
                {"icon": "\U0001F93F", "title": "Snorkel & sandbank stop", "description": "Time in the water over the reef, plus a stop on a sandbank exposed at low tide."},
                {"icon": "\U0001F37D\uFE0F", "title": "Seafood lunch on Wasini Island", "description": "A full seafood lunch at a local restaurant, with an optional village walk after."},
                {"icon": "\U0001F690", "title": "Return transfer", "description": "Drive back to your accommodation."},
            ],
            "de": [
                {"icon": "\U0001F3E8", "title": "Abholung & Fahrt nach Shimoni", "description": "Wir holen Sie an Ihrer Unterkunft ab und fahren etwa 90 Minuten nach Shimoni."},
                {"icon": "\u26F5", "title": "An Bord des Segelboots", "description": "Es geht hinaus in den Wasini-Kanal auf die Suche nach Delfinen."},
                {"icon": "\U0001F42C", "title": "Delfinbeobachtung", "description": "Sobald ein Schwarm gefunden ist, verlangsamt das Boot und folgt in respektvollem Abstand."},
                {"icon": "\U0001F93F", "title": "Schnorcheln & Sandbank", "description": "Zeit im Wasser über dem Riff, dazu ein Stopp auf einer Sandbank, die bei Ebbe zum Vorschein kommt."},
                {"icon": "\U0001F37D\uFE0F", "title": "Fischmenü auf Wasini Island", "description": "Ein vollständiges Fischmenü in einem lokalen Restaurant, danach optional ein Dorfspaziergang."},
                {"icon": "\U0001F690", "title": "Rücktransfer", "description": "Fahrt zurück zu Ihrer Unterkunft."},
            ],
            "fr": [
                {"icon": "\U0001F3E8", "title": "Prise en charge & route vers Shimoni", "description": "Nous venons vous chercher à votre hébergement et roulons environ 90 minutes jusqu'à Shimoni."},
                {"icon": "\u26F5", "title": "Embarquement sur le voilier", "description": "Direction le chenal de Wasini à la recherche des dauphins."},
                {"icon": "\U0001F42C", "title": "Observation des dauphins", "description": "Dès qu'un groupe est repéré, le bateau ralentit et le suit à distance respectueuse."},
                {"icon": "\U0001F93F", "title": "Plongée avec tuba & banc de sable", "description": "Temps dans l'eau au-dessus du récif, puis arrêt sur un banc de sable visible à marée basse."},
                {"icon": "\U0001F37D\uFE0F", "title": "Déjeuner de fruits de mer sur l'île de Wasini", "description": "Un déjeuner complet dans un restaurant local, avec une promenade optionnelle dans le village."},
                {"icon": "\U0001F690", "title": "Retour", "description": "Trajet retour vers votre hébergement."},
            ],
        },
    },
    {
        "slug": "sunset-canoe-trip",
        "accent": "gold",
        "emoji": "\U0001F6F6",
        "name": {
            "en": "Sunset Canoe Trip on the Congo River",
            "de": "Sonnenuntergangs-Kanutour am Congo River",
            "fr": "Balade en pirogue au coucher du soleil sur la rivière Congo",
        },
        "tagline": {
            "en": "Paddle the mangroves as the ocean meets the river",
            "de": "Durch die Mangroven paddeln, dort wo der Ozean auf den Fluss trifft",
            "fr": "Pagayer dans la mangrove là où l'océan rencontre la rivière",
        },
        "teaser": {
            "en": "An evening tuk-tuk ride to the Congo River, where the ocean meets the river, followed by a quiet hand-paddled canoe trip through the mangroves at sunset.",
            "de": "Eine abendliche Tuk-Tuk-Fahrt zum Congo River, wo der Ozean auf den Fluss trifft, gefolgt von einer ruhigen, handgepaddelten Kanutour durch die Mangroven bei Sonnenuntergang.",
            "fr": "Une balade en tuk-tuk en soirée jusqu'à la rivière Congo, là où l'océan rencontre la rivière, suivie d'une paisible balade en pirogue à travers la mangrove au coucher du soleil.",
        },
        "duration": {"en": "3 hours", "de": "3 Stunden", "fr": "3 heures"},
        "group_size": {
            "en": "Small groups",
            "de": "Kleine Gruppen",
            "fr": "Petits groupes",
        },
        "price": {
            "en": "€50 per person",
            "de": "50 € pro Person",
            "fr": "50 € par personne",
        },
        "difficulty": {
            "en": "Easy - suitable for all ages",
            "de": "Einfach - für alle Altersgruppen geeignet",
            "fr": "Facile - convient à tous les âges",
        },
        "departs": {
            "en": "4:30pm pick-up from your Diani accommodation",
            "de": "Abholung um 16:30 Uhr an Ihrer Unterkunft in Diani",
            "fr": "Prise en charge à 16h30 à votre hébergement à Diani",
        },
        "best_time": {"en": "Year-round", "de": "Ganzjährig", "fr": "Toute l'année"},
        "highlights": {
            "en": [
                "The point where the Indian Ocean meets the Congo River",
                "A traditional canoe, paddled by hand with no engine",
                "River birdlife and mangrove scenery at sunset",
                "Supports the local community - the crew also runs beach clean-ups",
            ],
            "de": [
                "Der Punkt, an dem der Indische Ozean auf den Congo River trifft",
                "Ein traditionelles Kanu, von Hand gepaddelt, ohne Motor",
                "Flussvögel und Mangrovenlandschaft bei Sonnenuntergang",
                "Unterstützt die lokale Gemeinschaft - das Team organisiert auch Strandreinigungen",
            ],
            "fr": [
                "Le point où l'océan Indien rencontre la rivière Congo",
                "Une pirogue traditionnelle, pagayée à la main, sans moteur",
                "Oiseaux de rivière et paysages de mangrove au coucher du soleil",
                "Soutient la communauté locale - l'équipe organise aussi des nettoyages de plage",
            ],
        },
        "overview": {
            "en": [
                "We pick you up by tuk-tuk at 4:30pm and head to a stretch of the "
                "Congo River where it meets the ocean. While the canoe is "
                "prepared, you can relax on the sand dunes with a drink and take "
                "in the view.",
                "The canoe trip itself is slow and quiet, powered entirely by the "
                "captain rather than an engine, giving you a close, peaceful look "
                "at the mangroves and the river birds that live among them. The "
                "trip also supports the local community: the same team keeps the "
                "beaches clear of litter and puts proceeds toward local "
                "healthcare and education.",
            ],
            "de": [
                "Wir holen Sie um 16:30 Uhr mit dem Tuk-Tuk ab und fahren zu "
                "einem Abschnitt des Congo River, wo dieser auf den Ozean "
                "trifft. Während das Kanu vorbereitet wird, können Sie auf den "
                "Sanddünen bei einem Getränk die Aussicht genießen.",
                "Die Kanutour selbst ist ruhig und langsam, vollständig von "
                "Hand gepaddelt ohne Motor, und bietet einen nahen, friedlichen "
                "Blick auf die Mangroven und die dort lebenden Flussvögel. Die "
                "Tour unterstützt zudem die lokale Gemeinschaft: Dasselbe Team "
                "hält die Strände sauber und investiert die Einnahmen in "
                "lokale Gesundheitsversorgung und Bildung.",
            ],
            "fr": [
                "Nous venons vous chercher en tuk-tuk à 16h30 et nous dirigeons "
                "vers un tronçon de la rivière Congo à l'endroit où elle "
                "rencontre l'océan. Pendant que la pirogue est préparée, vous "
                "pouvez profiter de la vue depuis les dunes de sable avec une "
                "boisson.",
                "La balade en pirogue elle-même est lente et paisible, "
                "entièrement pagayée à la main sans moteur, offrant une vue "
                "rapprochée et tranquille sur la mangrove et les oiseaux qui y "
                "vivent. Cette excursion soutient aussi la communauté locale : "
                "la même équipe entretient la propreté des plages et reverse "
                "une partie des recettes à la santé et à l'éducation locales.",
            ],
        },
        "included": {
            "en": [
                "Hotel shuttle",
                "Canoe trip and captain",
                "Tropical seasonal fruit, available on request",
            ],
            "de": [
                "Shuttle von der Unterkunft",
                "Kanutour mit Kapitän",
                "Tropische Saisonfrüchte auf Anfrage",
            ],
            "fr": [
                "Navette depuis l'hébergement",
                "Balade en pirogue avec capitaine",
                "Fruits tropicaux de saison, sur demande",
            ],
        },
        "excluded": {
            "en": ["Drinks", "Tips for the captain and crew"],
            "de": ["Getränke", "Trinkgeld für Kapitän und Team"],
            "fr": ["Boissons", "Pourboires pour le capitaine et l'équipe"],
        },
        "bring": {
            "en": [
                "A light jacket or shawl for the evening breeze",
                "Comfortable, closed shoes for getting in and out of the canoe",
                "A camera for the sunset",
            ],
            "de": [
                "Eine leichte Jacke oder ein Tuch für die Abendbrise",
                "Bequeme, geschlossene Schuhe zum Ein- und Aussteigen aus dem Kanu",
                "Eine Kamera für den Sonnenuntergang",
            ],
            "fr": [
                "Une veste légère ou un châle pour la brise du soir",
                "Des chaussures fermées et confortables pour monter et descendre de la pirogue",
                "Un appareil photo pour le coucher du soleil",
            ],
        },
        "itinerary": {
            "en": [
                {"icon": "\U0001F6FA", "title": "Tuk-tuk pick-up", "description": "Collected from your Diani accommodation at 4:30pm."},
                {"icon": "\U0001F3D6\uFE0F", "title": "Arrive at the river mouth", "description": "Relax on the sand dunes while the canoe is prepared."},
                {"icon": "\U0001F6F6", "title": "Canoe departs", "description": "A hand-paddled canoe heads up the river into the mangroves."},
                {"icon": "\U0001F426", "title": "Mangrove wildlife", "description": "Spot river birds along the quiet, engine-free stretch."},
                {"icon": "\U0001F307", "title": "Sunset on the water", "description": "The paddle times to catch the sun going down."},
                {"icon": "\U0001F6FA", "title": "Return transfer", "description": "Tuk-tuk back to your accommodation."},
            ],
            "de": [
                {"icon": "\U0001F6FA", "title": "Abholung mit dem Tuk-Tuk", "description": "Abholung an Ihrer Unterkunft in Diani um 16:30 Uhr."},
                {"icon": "\U0001F3D6\uFE0F", "title": "Ankunft an der Flussmündung", "description": "Entspannen Sie auf den Sanddünen, während das Kanu vorbereitet wird."},
                {"icon": "\U0001F6F6", "title": "Start der Kanutour", "description": "Ein handgepaddeltes Kanu fährt den Fluss hinauf in die Mangroven."},
                {"icon": "\U0001F426", "title": "Tierwelt der Mangroven", "description": "Beobachten Sie Flussvögel entlang des ruhigen, motorfreien Abschnitts."},
                {"icon": "\U0001F307", "title": "Sonnenuntergang auf dem Wasser", "description": "Die Fahrt ist so getimt, dass Sie den Sonnenuntergang miterleben."},
                {"icon": "\U0001F6FA", "title": "Rücktransfer", "description": "Tuk-Tuk zurück zu Ihrer Unterkunft."},
            ],
            "fr": [
                {"icon": "\U0001F6FA", "title": "Prise en charge en tuk-tuk", "description": "Prise en charge à votre hébergement à Diani à 16h30."},
                {"icon": "\U0001F3D6\uFE0F", "title": "Arrivée à l'embouchure de la rivière", "description": "Détendez-vous sur les dunes de sable pendant la préparation de la pirogue."},
                {"icon": "\U0001F6F6", "title": "Départ en pirogue", "description": "Une pirogue pagayée à la main remonte la rivière dans la mangrove."},
                {"icon": "\U0001F426", "title": "Faune de la mangrove", "description": "Observez les oiseaux de rivière le long de ce tronçon calme et sans moteur."},
                {"icon": "\U0001F307", "title": "Coucher de soleil sur l'eau", "description": "La balade est chronométrée pour profiter du coucher du soleil."},
                {"icon": "\U0001F6FA", "title": "Retour", "description": "Tuk-tuk retour vers votre hébergement."},
            ],
        },
    },
    {
        "slug": "glass-bottom-boat-trip",
        "accent": "ocean",
        "emoji": "\U0001F420",
        "name": {
            "en": "Glass-Bottom Boat Trip",
            "de": "Bootsfahrt mit Glasboden",
            "fr": "Sortie en bateau à fond de verre",
        },
        "tagline": {
            "en": "See the reef without getting your hair wet",
            "de": "Das Riff sehen, ohne nass zu werden",
            "fr": "Voir le récif sans se mouiller les cheveux",
        },
        "teaser": {
            "en": "A relaxed trip from Diani Beach over the coral garden, with a glass-bottom boat so non-swimmers and young children can see the reef too.",
            "de": "Eine entspannte Fahrt vom Diani Beach über den Korallengarten - dank Glasbodenboot können auch Nichtschwimmer und kleine Kinder das Riff sehen.",
            "fr": "Une sortie tranquille depuis Diani Beach au-dessus du jardin de corail, en bateau à fond de verre afin que les non-nageurs et les jeunes enfants puissent aussi voir le récif.",
        },
        "duration": {"en": "Half day", "de": "Halbtägig", "fr": "Demi-journée"},
        "group_size": {
            "en": "Small groups",
            "de": "Kleine Gruppen",
            "fr": "Petits groupes",
        },
        "price": {
            "en": "€30 per person",
            "de": "30 € pro Person",
            "fr": "30 € par personne",
        },
        "difficulty": {
            "en": "Easy - suitable for all ages (children must be supervised)",
            "de": "Einfach - für alle Altersgruppen geeignet (Kinder müssen beaufsichtigt werden)",
            "fr": "Facile - convient à tous les âges (enfants sous surveillance)",
        },
        "departs": {
            "en": "Departs from Diani Beach",
            "de": "Abfahrt ab Diani Beach",
            "fr": "Départ depuis Diani Beach",
        },
        "best_time": {
            "en": "Year-round; best visibility at low tide",
            "de": "Ganzjährig; beste Sicht bei Ebbe",
            "fr": "Toute l'année ; meilleure visibilité à marée basse",
        },
        "highlights": {
            "en": [
                "A protected coral garden just off Diani Beach",
                "Glass-bottom viewing for non-swimmers and young children",
                "A sandbank that appears at low tide",
                "Snorkeling included for those who want to get in the water",
            ],
            "de": [
                "Ein geschützter Korallengarten direkt vor Diani Beach",
                "Glasboden-Ansicht für Nichtschwimmer und kleine Kinder",
                "Eine Sandbank, die bei Ebbe zum Vorschein kommt",
                "Schnorcheln inklusive für alle, die ins Wasser möchten",
            ],
            "fr": [
                "Un jardin de corail protégé juste au large de Diani Beach",
                "Vue à travers le fond de verre pour les non-nageurs et les jeunes enfants",
                "Un banc de sable qui apparaît à marée basse",
                "Plongée avec tuba incluse pour ceux qui souhaitent se mettre à l'eau",
            ],
        },
        "overview": {
            "en": [
                "This is one of the simplest ways to see Diani's underwater "
                "world. We sail out over the reef in a glass-bottom boat, so "
                "even non-swimmers get a clear view of the coral and fish below "
                "without leaving the boat.",
                "For anyone who wants to get in the water, there's time to "
                "snorkel over the coral garden and to rest on a sandbank that "
                "only shows itself at low tide. Bring an underwater camera if "
                "you have one - the coral and fish here are some of the most "
                "colourful on this stretch of coast.",
            ],
            "de": [
                "Dies ist eine der einfachsten Arten, die Unterwasserwelt von "
                "Diani zu entdecken. Wir fahren mit einem Glasbodenboot über "
                "das Riff, sodass selbst Nichtschwimmer einen klaren Blick auf "
                "Korallen und Fische darunter haben, ohne das Boot zu "
                "verlassen.",
                "Wer ins Wasser möchte, kann über dem Korallengarten "
                "schnorcheln und sich auf einer Sandbank ausruhen, die nur bei "
                "Ebbe zum Vorschein kommt. Bringen Sie gerne eine "
                "Unterwasserkamera mit - die Korallen und Fische hier gehören "
                "zu den farbenprächtigsten an dieser Küste.",
            ],
            "fr": [
                "C'est l'une des façons les plus simples de découvrir les "
                "fonds marins de Diani. Nous naviguons au-dessus du récif dans "
                "un bateau à fond de verre, permettant même aux non-nageurs "
                "d'observer clairement le corail et les poissons sans quitter "
                "le bateau.",
                "Pour ceux qui souhaitent se mettre à l'eau, il y a du temps "
                "pour faire de la plongée avec tuba au-dessus du jardin de "
                "corail et se reposer sur un banc de sable qui n'apparaît qu'à "
                "marée basse. Apportez un appareil photo étanche si vous en "
                "avez un - le corail et les poissons ici comptent parmi les "
                "plus colorés de cette côte.",
            ],
        },
        "included": {
            "en": [
                "Accommodation pick-up",
                "Boat captain and crew",
                "Snorkeling guide",
                "Snorkeling equipment (mask and snorkel)",
            ],
            "de": [
                "Abholung von der Unterkunft",
                "Bootskapitän und Crew",
                "Schnorchelguide",
                "Schnorchelausrüstung (Maske und Schnorchel)",
            ],
            "fr": [
                "Prise en charge à l'hébergement",
                "Capitaine et équipage",
                "Guide de plongée avec tuba",
                "Équipement de plongée avec tuba (masque et tuba)",
            ],
        },
        "excluded": {
            "en": ["Drinks", "Tips for the crew and guide"],
            "de": ["Getränke", "Trinkgeld für Crew und Guide"],
            "fr": ["Boissons", "Pourboires pour l'équipage et le guide"],
        },
        "bring": {
            "en": [
                "Swimwear and a rash guard",
                "Reef-safe sunscreen",
                "An underwater camera, if you have one",
                "A hat and sunglasses",
            ],
            "de": [
                "Badebekleidung und ein UV-Shirt",
                "Riffverträglichen Sonnenschutz",
                "Eine Unterwasserkamera, falls vorhanden",
                "Hut und Sonnenbrille",
            ],
            "fr": [
                "Maillot de bain et un tee-shirt anti-UV",
                "Crème solaire respectueuse des récifs",
                "Un appareil photo étanche, si vous en avez un",
                "Un chapeau et des lunettes de soleil",
            ],
        },
        "itinerary": {
            "en": [
                {"icon": "\U0001F3E8", "title": "Pick-up", "description": "Collected from your accommodation."},
                {"icon": "\u26F5", "title": "Boat departs Diani Beach", "description": "Head out over the coral garden."},
                {"icon": "\U0001F420", "title": "Glass-bottom viewing", "description": "Watch the reef and fish through the boat's glass panel."},
                {"icon": "\U0001F93F", "title": "Optional snorkel & sandbank", "description": "Time in the water for anyone who wants a closer look, plus a stop on a sandbank at low tide."},
                {"icon": "\U0001F3E8", "title": "Return transfer", "description": "Back to your accommodation."},
            ],
            "de": [
                {"icon": "\U0001F3E8", "title": "Abholung", "description": "Abholung an Ihrer Unterkunft."},
                {"icon": "\u26F5", "title": "Abfahrt ab Diani Beach", "description": "Es geht hinaus über den Korallengarten."},
                {"icon": "\U0001F420", "title": "Blick durch den Glasboden", "description": "Beobachten Sie Riff und Fische durch die Glasscheibe des Boots."},
                {"icon": "\U0001F93F", "title": "Optionales Schnorcheln & Sandbank", "description": "Zeit im Wasser für alle, die es genauer sehen möchten, dazu ein Stopp auf einer Sandbank bei Ebbe."},
                {"icon": "\U0001F3E8", "title": "Rücktransfer", "description": "Zurück zu Ihrer Unterkunft."},
            ],
            "fr": [
                {"icon": "\U0001F3E8", "title": "Prise en charge", "description": "Prise en charge à votre hébergement."},
                {"icon": "\u26F5", "title": "Départ depuis Diani Beach", "description": "Direction le jardin de corail."},
                {"icon": "\U0001F420", "title": "Vue à travers le fond de verre", "description": "Observez le récif et les poissons à travers la vitre du bateau."},
                {"icon": "\U0001F93F", "title": "Plongée optionnelle & banc de sable", "description": "Temps dans l'eau pour ceux qui veulent voir de plus près, avec un arrêt sur un banc de sable à marée basse."},
                {"icon": "\U0001F3E8", "title": "Retour", "description": "Retour vers votre hébergement."},
            ],
        },
    },
    {
        "slug": "romantic-canoe-trip",
        "accent": "indigo",
        "emoji": "\U0001F495",
        "name": {
            "en": "Romantic Canoe Boat Trip",
            "de": "Romantische Kanutour",
            "fr": "Balade romantique en pirogue",
        },
        "tagline": {
            "en": "A hidden sandbank and reef, just for two",
            "de": "Eine versteckte Sandbank und ein Riff, nur für zwei",
            "fr": "Un banc de sable et un récif cachés, rien que pour deux",
        },
        "teaser": {
            "en": "A quiet, hand-paddled canoe trip from Diani Beach to a hidden sandbank and reef most visitors never find - a favourite for couples.",
            "de": "Eine ruhige, handgepaddelte Kanutour vom Diani Beach zu einer versteckten Sandbank und einem Riff, das die meisten Besucher nie finden - ein Favorit für Paare.",
            "fr": "Une paisible balade en pirogue depuis Diani Beach jusqu'à un banc de sable et un récif cachés que la plupart des visiteurs ne trouvent jamais - un favori pour les couples.",
        },
        "duration": {"en": "Half day", "de": "Halbtägig", "fr": "Demi-journée"},
        "group_size": {
            "en": "Private for couples or small groups",
            "de": "Privat für Paare oder kleine Gruppen",
            "fr": "Privé pour couples ou petits groupes",
        },
        "price": {
            "en": "€30 per person",
            "de": "30 € pro Person",
            "fr": "30 € par personne",
        },
        "difficulty": {
            "en": "Easy - suitable for all ages",
            "de": "Einfach - für alle Altersgruppen geeignet",
            "fr": "Facile - convient à tous les âges",
        },
        "departs": {
            "en": "Pick-up from your Diani accommodation",
            "de": "Abholung an Ihrer Unterkunft in Diani",
            "fr": "Prise en charge à votre hébergement à Diani",
        },
        "best_time": {
            "en": "Year-round; best at low tide",
            "de": "Ganzjährig; am besten bei Ebbe",
            "fr": "Toute l'année ; idéal à marée basse",
        },
        "highlights": {
            "en": [
                "A hidden sandbank, exposed only at low tide",
                "An unusually colourful, rarely-visited patch of reef",
                "A hand-paddled canoe with no engine noise",
                "Zebrafish, lionfish, moray eels, octopus and lobster on the reef",
            ],
            "de": [
                "Eine versteckte Sandbank, die nur bei Ebbe sichtbar ist",
                "Ein ungewöhnlich farbenprächtiges, selten besuchtes Riff",
                "Ein handgepaddeltes Kanu ohne Motorenlärm",
                "Zebrafische, Rotfeuerfische, Muränen, Oktopusse und Langusten am Riff",
            ],
            "fr": [
                "Un banc de sable caché, visible uniquement à marée basse",
                "Un récif étonnamment coloré et rarement visité",
                "Une pirogue pagayée à la main, sans bruit de moteur",
                "Poissons-zèbres, poissons-lions, murènes, poulpes et langoustes sur le récif",
            ],
        },
        "overview": {
            "en": [
                "From Diani Beach, we paddle out to a sandbank that only appears "
                "at low tide - a quiet spot most visitors never get to, since "
                "it's only reachable by canoe. Because so few people snorkel "
                "here, the reef is noticeably more colourful and undisturbed "
                "than busier spots along the coast.",
                "Between snorkels, you can simply lie back on the sandbank "
                "itself. It's an easy, unhurried few hours, and one of our most "
                "popular trips for couples looking for something quieter than a "
                "full-day excursion.",
            ],
            "de": [
                "Vom Diani Beach aus paddeln wir zu einer Sandbank, die nur "
                "bei Ebbe zum Vorschein kommt - ein ruhiger Ort, den die "
                "meisten Besucher nie erreichen, da er nur mit dem Kanu "
                "zugänglich ist. Weil hier so wenige Menschen schnorcheln, ist "
                "das Riff spürbar farbenprächtiger und unberührter als an "
                "belebteren Stellen der Küste.",
                "Zwischen den Schnorchelgängen können Sie einfach auf der "
                "Sandbank entspannen. Es ist ein unkomplizierter, entspannter "
                "Ausflug von wenigen Stunden und eine unserer beliebtesten "
                "Touren für Paare, die etwas Ruhigeres als einen ganztägigen "
                "Ausflug suchen.",
            ],
            "fr": [
                "Depuis Diani Beach, nous pagayons jusqu'à un banc de sable "
                "qui n'apparaît qu'à marée basse - un lieu paisible que la "
                "plupart des visiteurs n'atteignent jamais, accessible "
                "uniquement en pirogue. Comme très peu de monde y plonge avec "
                "tuba, le récif est nettement plus coloré et préservé que les "
                "sites plus fréquentés de la côte.",
                "Entre deux sessions de plongée, vous pouvez simplement vous "
                "détendre sur le banc de sable. C'est une sortie simple et "
                "tranquille de quelques heures, et l'une de nos excursions "
                "préférées des couples en quête de calme, loin d'une "
                "excursion d'une journée complète.",
            ],
        },
        "included": {
            "en": [
                "Snorkeling equipment (mask and snorkel)",
                "Captain and a snorkeling guide",
                "Transfers to and from your accommodation",
            ],
            "de": [
                "Schnorchelausrüstung (Maske und Schnorchel)",
                "Kapitän und Schnorchelguide",
                "Transfer von und zur Unterkunft",
            ],
            "fr": [
                "Équipement de plongée avec tuba (masque et tuba)",
                "Capitaine et guide de plongée",
                "Transferts depuis et vers l'hébergement",
            ],
        },
        "excluded": {
            "en": ["Drinks", "Tips for the captain and guide"],
            "de": ["Getränke", "Trinkgeld für Kapitän und Guide"],
            "fr": ["Boissons", "Pourboires pour le capitaine et le guide"],
        },
        "bring": {
            "en": [
                "Swimwear and a light cover-up",
                "Reef-safe sunscreen",
                "A towel",
            ],
            "de": [
                "Badebekleidung und einen leichten Überwurf",
                "Riffverträglichen Sonnenschutz",
                "Ein Handtuch",
            ],
            "fr": [
                "Maillot de bain et une tenue légère",
                "Crème solaire respectueuse des récifs",
                "Une serviette",
            ],
        },
        "itinerary": {
            "en": [
                {"icon": "\U0001F3E8", "title": "Pick-up", "description": "Collected from your Diani accommodation."},
                {"icon": "\U0001F6F6", "title": "Canoe departs", "description": "Paddle out from Diani Beach toward a hidden sandbank."},
                {"icon": "\U0001F93F", "title": "Snorkel stop", "description": "Time over a quiet, rarely-visited patch of reef."},
                {"icon": "\U0001F3D6\uFE0F", "title": "Sandbank relaxation", "description": "Unwind on the sandbank between snorkels."},
                {"icon": "\U0001F3E8", "title": "Return", "description": "Paddle back and transfer to your accommodation."},
            ],
            "de": [
                {"icon": "\U0001F3E8", "title": "Abholung", "description": "Abholung an Ihrer Unterkunft in Diani."},
                {"icon": "\U0001F6F6", "title": "Start der Kanutour", "description": "Vom Diani Beach aus geht es zu einer versteckten Sandbank."},
                {"icon": "\U0001F93F", "title": "Schnorchelstopp", "description": "Zeit über einem ruhigen, selten besuchten Riffabschnitt."},
                {"icon": "\U0001F3D6\uFE0F", "title": "Entspannung auf der Sandbank", "description": "Entspannen Sie zwischen den Schnorchelgängen auf der Sandbank."},
                {"icon": "\U0001F3E8", "title": "Rückkehr", "description": "Zurückpaddeln und Transfer zu Ihrer Unterkunft."},
            ],
            "fr": [
                {"icon": "\U0001F3E8", "title": "Prise en charge", "description": "Prise en charge à votre hébergement à Diani."},
                {"icon": "\U0001F6F6", "title": "Départ en pirogue", "description": "Départ depuis Diani Beach vers un banc de sable caché."},
                {"icon": "\U0001F93F", "title": "Arrêt plongée avec tuba", "description": "Temps au-dessus d'un tronçon de récif calme et peu fréquenté."},
                {"icon": "\U0001F3D6\uFE0F", "title": "Détente sur le banc de sable", "description": "Détendez-vous sur le banc de sable entre deux sessions de plongée."},
                {"icon": "\U0001F3E8", "title": "Retour", "description": "Retour en pirogue puis transfert vers votre hébergement."},
            ],
        },
    },
    {
        "slug": "deep-sea-fishing",
        "accent": "coral",
        "emoji": "\U0001F3A3",
        "name": {
            "en": "Wild Fishing in Diani",
            "de": "Hochseeangeln in Diani",
            "fr": "Pêche sportive à Diani",
        },
        "tagline": {
            "en": "Offshore sport fishing for tuna, marlin and sailfish",
            "de": "Sportfischen auf Thunfisch, Marlin und Segelfisch",
            "fr": "Pêche sportive au large pour thon, marlin et voilier",
        },
        "teaser": {
            "en": "A day of offshore sport fishing from Diani, chasing tuna, shark, swordfish, marlin and sailfish - catch, tag or release, your choice.",
            "de": "Ein Tag Hochsee-Sportfischen ab Diani, auf der Jagd nach Thunfisch, Hai, Schwertfisch, Marlin und Segelfisch - fangen, markieren oder freilassen, ganz nach Wahl.",
            "fr": "Une journée de pêche sportive au large depuis Diani, à la recherche de thon, requin, espadon, marlin et voilier - attraper, marquer ou relâcher, à votre choix.",
        },
        "duration": {
            "en": "4, 6, 8 or 10 hours - you choose",
            "de": "4, 6, 8 oder 10 Stunden - Sie entscheiden",
            "fr": "4, 6, 8 ou 10 heures - à vous de choisir",
        },
        "group_size": {
            "en": "4 - 6 anglers per boat",
            "de": "4 - 6 Angler pro Boot",
            "fr": "4 à 6 pêcheurs par bateau",
        },
        "price": {
            "en": "€450 - €1,100 per trip",
            "de": "450 € - 1.100 € pro Ausfahrt",
            "fr": "450 € - 1 100 € par sortie",
        },
        "difficulty": {
            "en": "Moderate - open to first-timers and experienced anglers",
            "de": "Mittel - geeignet für Anfänger und erfahrene Angler",
            "fr": "Modéré - accessible aux débutants comme aux pêcheurs expérimentés",
        },
        "departs": {
            "en": "6:30am, Diani Beach",
            "de": "6:30 Uhr, Diani Beach",
            "fr": "6h30, Diani Beach",
        },
        "best_time": {"en": "Year-round", "de": "Ganzjährig", "fr": "Toute l'année"},
        "highlights": {
            "en": [
                "Boats built for offshore sport fishing, 4-6 anglers per trip",
                "Tuna, shark, swordfish, marlin and sailfish grounds",
                "Catch, tag or release - your choice",
                "Suitable for both first-time and experienced anglers",
            ],
            "de": [
                "Boote für Hochsee-Sportfischen, 4-6 Angler pro Ausfahrt",
                "Reviere für Thunfisch, Hai, Schwertfisch, Marlin und Segelfisch",
                "Fangen, markieren oder freilassen - Ihre Wahl",
                "Geeignet für Einsteiger und erfahrene Angler",
            ],
            "fr": [
                "Bateaux conçus pour la pêche sportive au large, 4 à 6 pêcheurs par sortie",
                "Zones de pêche au thon, requin, espadon, marlin et voilier",
                "Attraper, marquer ou relâcher - à votre choix",
                "Convient aussi bien aux débutants qu'aux pêcheurs expérimentés",
            ],
        },
        "overview": {
            "en": [
                "We head out early, at 6:30am, to reach the fishing grounds "
                "while conditions are calmest, keeping an eye out for dolphins "
                "along the way. Whether you're an experienced angler or trying "
                "it for the first time, the crew will get you set up and fishing "
                "quickly.",
                "Depending on the day and season, you can expect a shot at tuna, "
                "shark, swordfish, marlin and sailfish. It's entirely your call "
                "whether you keep, tag or release what you catch.",
                "Pricing is per trip, shared by up to 6 anglers, not per person: "
                "€450 for 4 hours, €650 for 6 hours, €850 for 8 hours, or €1,100 "
                "for 10 hours - book the length that suits your day and budget.",
            ],
            "de": [
                "Wir starten früh um 6:30 Uhr, um die Fanggründe bei "
                "ruhigsten Bedingungen zu erreichen, und halten unterwegs "
                "Ausschau nach Delfinen. Ob erfahrener Angler oder "
                "Erstversuch - die Crew richtet Sie schnell für den Fang ein.",
                "Je nach Tag und Saison können Sie mit Thunfisch, Hai, "
                "Schwertfisch, Marlin und Segelfisch rechnen. Ob Sie Ihren "
                "Fang behalten, markieren oder freilassen, entscheiden ganz "
                "Sie.",
                "Die Preise gelten pro Ausfahrt, aufgeteilt auf bis zu 6 "
                "Angler, nicht pro Person: 450 € für 4 Stunden, 650 € für 6 "
                "Stunden, 850 € für 8 Stunden oder 1.100 € für 10 Stunden - "
                "buchen Sie die Dauer, die zu Ihrem Tag und Budget passt.",
            ],
            "fr": [
                "Nous partons tôt, à 6h30, pour atteindre les zones de pêche "
                "pendant que les conditions sont les plus calmes, en gardant "
                "un œil sur d'éventuels dauphins en chemin. Que vous soyez un "
                "pêcheur expérimenté ou que vous essayiez pour la première "
                "fois, l'équipage vous installera rapidement.",
                "Selon le jour et la saison, vous pourrez tenter votre chance "
                "avec le thon, le requin, l'espadon, le marlin et le voilier. "
                "Vous êtes entièrement libre de garder, marquer ou relâcher "
                "votre prise.",
                "Les tarifs sont par sortie, partagés entre 6 pêcheurs "
                "maximum, et non par personne : 450 € pour 4 heures, 650 € "
                "pour 6 heures, 850 € pour 8 heures, ou 1 100 € pour 10 "
                "heures - réservez la durée qui correspond à votre journée et "
                "à votre budget.",
            ],
        },
        "included": {
            "en": [
                "Transfers to and from your accommodation",
                "Fruit and soft drinks on board",
                "Fishing equipment",
            ],
            "de": [
                "Transfer von und zur Unterkunft",
                "Obst und alkoholfreie Getränke an Bord",
                "Angelausrüstung",
            ],
            "fr": [
                "Transferts depuis et vers l'hébergement",
                "Fruits et boissons non alcoolisées à bord",
                "Matériel de pêche",
            ],
        },
        "excluded": {
            "en": ["Alcoholic drinks", "Tips for the captain and crew"],
            "de": ["Alkoholische Getränke", "Trinkgeld für Kapitän und Crew"],
            "fr": ["Boissons alcoolisées", "Pourboires pour le capitaine et l'équipage"],
        },
        "bring": {
            "en": [
                "A hat, sunglasses and reef-safe sunscreen",
                "Light long sleeves for sun protection",
                "Motion sickness tablets if you're prone to seasickness",
            ],
            "de": [
                "Hut, Sonnenbrille und riffverträglichen Sonnenschutz",
                "Leichte, langärmelige Kleidung als Sonnenschutz",
                "Reisetabletten gegen Seekrankheit, falls anfällig",
            ],
            "fr": [
                "Un chapeau, des lunettes de soleil et une crème solaire respectueuse des récifs",
                "Des vêtements légers à manches longues pour se protéger du soleil",
                "Des comprimés contre le mal de mer si vous y êtes sujet",
            ],
        },
        "itinerary": {
            "en": [
                {"icon": "\U0001F3E8", "title": "Early pick-up", "description": "Collected from your accommodation at 6:30am."},
                {"icon": "\u26F5", "title": "Head to the fishing grounds", "description": "The boat runs out to open water, watching for dolphins on the way."},
                {"icon": "\U0001F3A3", "title": "Fishing begins", "description": "The crew sets up tackle and starts trolling for tuna, marlin, sailfish and more."},
                {"icon": "\U0001F41F", "title": "Catch, tag or release", "description": "Reel in your catch and decide what happens next."},
                {"icon": "\U0001F3E8", "title": "Return transfer", "description": "Fish cleaned and bagged, then back to your accommodation."},
            ],
            "de": [
                {"icon": "\U0001F3E8", "title": "Frühe Abholung", "description": "Abholung an Ihrer Unterkunft um 6:30 Uhr."},
                {"icon": "\u26F5", "title": "Fahrt zu den Fanggründen", "description": "Das Boot fährt hinaus aufs offene Wasser, unterwegs wird nach Delfinen Ausschau gehalten."},
                {"icon": "\U0001F3A3", "title": "Der Fang beginnt", "description": "Die Crew rüstet die Ausrüstung und beginnt mit dem Schleppfischen auf Thunfisch, Marlin, Segelfisch und mehr."},
                {"icon": "\U0001F41F", "title": "Fangen, markieren oder freilassen", "description": "Holen Sie Ihren Fang ein und entscheiden Sie, was damit geschieht."},
                {"icon": "\U0001F3E8", "title": "Rücktransfer", "description": "Der Fisch wird ausgenommen und verpackt, dann geht es zurück zu Ihrer Unterkunft."},
            ],
            "fr": [
                {"icon": "\U0001F3E8", "title": "Prise en charge matinale", "description": "Prise en charge à votre hébergement à 6h30."},
                {"icon": "\u26F5", "title": "Direction les zones de pêche", "description": "Le bateau file vers le large, en guettant d'éventuels dauphins en chemin."},
                {"icon": "\U0001F3A3", "title": "Début de la pêche", "description": "L'équipage installe le matériel et commence à traîner les lignes pour le thon, le marlin, le voilier et plus encore."},
                {"icon": "\U0001F41F", "title": "Attraper, marquer ou relâcher", "description": "Ramenez votre prise et décidez de son sort."},
                {"icon": "\U0001F3E8", "title": "Retour", "description": "Le poisson est nettoyé et emballé, puis retour vers votre hébergement."},
            ],
        },
    },
    {
        "slug": "jetski-safari",
        "accent": "sky",
        "emoji": "\U0001F6A4",
        "name": {
            "en": "Jet Ski Safari",
            "de": "Jetski-Safari",
            "fr": "Safari en jet-ski",
        },
        "tagline": {
            "en": "A fast, guided ride along the Diani coastline",
            "de": "Eine schnelle, geführte Fahrt entlang der Küste von Diani",
            "fr": "Une balade rapide et guidée le long de la côte de Diani",
        },
        "teaser": {
            "en": "A short, adrenaline-filled jet ski ride from Diani Beach, guided out through the reef channel to open water along the coast.",
            "de": "Eine kurze, actiongeladene Jetski-Fahrt ab Diani Beach, geführt durch den Riffkanal hinaus ins offene Wasser entlang der Küste.",
            "fr": "Une courte balade en jet-ski riche en adrénaline depuis Diani Beach, guidée à travers le chenal du récif jusqu'en eau libre le long de la côte.",
        },
        "duration": {
            "en": "30 or 60 minutes",
            "de": "30 oder 60 Minuten",
            "fr": "30 ou 60 minutes",
        },
        "group_size": {
            "en": "Single or double (tandem) jet ski",
            "de": "Einzel- oder Tandem-Jetski",
            "fr": "Jet-ski simple ou en tandem",
        },
        "price": {
            "en": "From €45 (30 min)",
            "de": "Ab 45 € (30 Min.)",
            "fr": "À partir de 45 € (30 min)",
        },
        "difficulty": {
            "en": "Easy - no experience needed, quick briefing included",
            "de": "Einfach - keine Erfahrung nötig, kurze Einweisung inklusive",
            "fr": "Facile - aucune expérience requise, brève initiation incluse",
        },
        "departs": {
            "en": "Diani Beach, daytime departures",
            "de": "Diani Beach, tagsüber",
            "fr": "Diani Beach, départs en journée",
        },
        "best_time": {
            "en": "Best at mid-to-high tide, when there's enough water over the reef",
            "de": "Am besten bei mittlerer bis hoher Flut, wenn genug Wasser über dem Riff steht",
            "fr": "Idéal à marée mi-haute à haute, lorsqu'il y a assez d'eau au-dessus du récif",
        },
        "highlights": {
            "en": [
                "A short briefing and practice run before you head out",
                "A guide leads you out through the reef channel to open water",
                "Tandem option if you'd rather ride as a passenger",
                "One of the quickest ways to get out on the water for an hour or less",
            ],
            "de": [
                "Kurze Einweisung und Probefahrt vor der Abfahrt",
                "Ein Guide führt Sie durch den Riffkanal hinaus ins offene Wasser",
                "Tandem-Option, falls Sie lieber als Beifahrer mitfahren möchten",
                "Eine der schnellsten Arten, für eine Stunde oder weniger aufs Wasser zu kommen",
            ],
            "fr": [
                "Une courte initiation et un essai avant de partir",
                "Un guide vous accompagne à travers le chenal du récif jusqu'en eau libre",
                "Option tandem si vous préférez être passager",
                "L'une des façons les plus rapides de profiter de l'eau en une heure ou moins",
            ],
        },
        "overview": {
            "en": [
                "Diani's reef sits close to shore, so every jet ski trip starts "
                "with a short briefing on the beach and a guide leading you out "
                "through a marked channel in the reef - the safest way through "
                "the shallows, especially if you've never ridden before.",
                "Once you're clear of the reef, you're free to open up along "
                "the coastline for the rest of your session. It's one of the "
                "shortest, most straightforward ways to get out on the water, "
                "and works well as a stand-alone activity or a quick add-on "
                "before or after a longer trip.",
            ],
            "de": [
                "Das Riff von Diani liegt nah an der Küste, daher beginnt "
                "jede Jetski-Fahrt mit einer kurzen Einweisung am Strand, bei "
                "der ein Guide Sie durch einen markierten Kanal im Riff führt "
                "- der sicherste Weg durch die Untiefen, besonders wenn Sie "
                "noch nie Jetski gefahren sind.",
                "Sobald Sie das Riff hinter sich gelassen haben, können Sie "
                "für den Rest Ihrer Session frei entlang der Küste fahren. Es "
                "ist eine der kürzesten, unkompliziertesten Arten, aufs "
                "Wasser zu kommen, und eignet sich sowohl als eigenständige "
                "Aktivität als auch als kurze Ergänzung vor oder nach einer "
                "längeren Tour.",
            ],
            "fr": [
                "Le récif de Diani se trouve tout près du rivage, c'est "
                "pourquoi chaque sortie en jet-ski commence par une courte "
                "initiation sur la plage, avec un guide qui vous accompagne à "
                "travers un chenal balisé dans le récif - le moyen le plus "
                "sûr de traverser les hauts-fonds, surtout si vous n'avez "
                "jamais fait de jet-ski.",
                "Une fois le récif passé, vous êtes libre d'accélérer le "
                "long de la côte pour le reste de votre session. C'est l'une "
                "des façons les plus rapides et les plus simples de profiter "
                "de l'eau, que ce soit comme activité à part entière ou en "
                "complément rapide avant ou après une excursion plus longue.",
            ],
        },
        "included": {
            "en": [
                "Pick-up and drop-off along Diani Beach Road",
                "Life jacket and a short briefing/practice run",
                "Guide to lead you out through the reef channel",
                "Fuel for your session",
            ],
            "de": [
                "Abholung und Rücktransfer entlang der Diani Beach Road",
                "Schwimmweste und kurze Einweisung/Probefahrt",
                "Guide, der Sie durch den Riffkanal führt",
                "Treibstoff für Ihre Session",
            ],
            "fr": [
                "Prise en charge et retour le long de Diani Beach Road",
                "Gilet de sauvetage et courte initiation/essai",
                "Guide vous accompagnant à travers le chenal du récif",
                "Carburant pour votre session",
            ],
        },
        "excluded": {
            "en": [
                "Photos/video (available on request from some operators)",
                "Tips for the guide",
            ],
            "de": [
                "Fotos/Videos (bei manchen Anbietern auf Anfrage erhältlich)",
                "Trinkgeld für den Guide",
            ],
            "fr": [
                "Photos/vidéos (disponibles sur demande selon les prestataires)",
                "Pourboire pour le guide",
            ],
        },
        "bring": {
            "en": [
                "Swimwear",
                "A rash guard or t-shirt (sun and spray protection)",
                "Reef-safe sunscreen",
                "A strap or dry pouch to secure glasses, if worn",
            ],
            "de": [
                "Badebekleidung",
                "Ein UV-Shirt oder T-Shirt (Sonnen- und Spritzschutz)",
                "Riffverträglichen Sonnenschutz",
                "Ein Band oder eine wasserdichte Hülle, um eine Brille zu sichern, falls getragen",
            ],
            "fr": [
                "Un maillot de bain",
                "Un tee-shirt anti-UV (protection contre le soleil et les embruns)",
                "Une crème solaire respectueuse des récifs",
                "Une sangle ou une pochette étanche pour sécuriser vos lunettes, le cas échéant",
            ],
        },
        "itinerary": {
            "en": [
                {"icon": "\U0001F3E8", "title": "Pick-up", "description": "Collected from along Diani Beach Road."},
                {"icon": "\U0001F9BA", "title": "Safety briefing", "description": "A short briefing and practice run on the beach."},
                {"icon": "\U0001F6A4", "title": "Guided reef crossing", "description": "A guide leads you out through a marked channel in the reef."},
                {"icon": "\U0001F30A", "title": "Open water ride", "description": "Open up along the coastline for the rest of your session."},
                {"icon": "\U0001F3E8", "title": "Return transfer", "description": "Back to your accommodation."},
            ],
            "de": [
                {"icon": "\U0001F3E8", "title": "Abholung", "description": "Abholung entlang der Diani Beach Road."},
                {"icon": "\U0001F9BA", "title": "Sicherheitseinweisung", "description": "Eine kurze Einweisung und Probefahrt am Strand."},
                {"icon": "\U0001F6A4", "title": "Geführte Durchfahrt durchs Riff", "description": "Ein Guide führt Sie durch einen markierten Kanal im Riff."},
                {"icon": "\U0001F30A", "title": "Fahrt im offenen Wasser", "description": "Für den Rest Ihrer Session geht es frei entlang der Küste."},
                {"icon": "\U0001F3E8", "title": "Rücktransfer", "description": "Zurück zu Ihrer Unterkunft."},
            ],
            "fr": [
                {"icon": "\U0001F3E8", "title": "Prise en charge", "description": "Prise en charge le long de Diani Beach Road."},
                {"icon": "\U0001F9BA", "title": "Briefing de sécurité", "description": "Une courte initiation et un essai sur la plage."},
                {"icon": "\U0001F6A4", "title": "Traversée guidée du récif", "description": "Un guide vous accompagne à travers un chenal balisé dans le récif."},
                {"icon": "\U0001F30A", "title": "Balade en eau libre", "description": "Vous êtes libre d'accélérer le long de la côte pour le reste de la session."},
                {"icon": "\U0001F3E8", "title": "Retour", "description": "Retour vers votre hébergement."},
            ],
        },
    },
]


# NOTE ON PRICING/TIMING FOR THE JET SKI SAFARI: unlike the other five
# excursions above (sourced from the operator's real excursions page),
# this entry was written from general knowledge of how jet ski rentals
# typically run on Diani Beach - short, tide-dependent, guided sessions
# through a marked reef channel. The specific price (€45/30 min) and
# duration options are a reasonable placeholder, not confirmed real
# rates. Double-check and update them before this goes live.


TESTIMONIALS = [
    {
        "trip_slug": "wasini-island-safari",
        "name": "Anke V.",
        "quote": {
            "en": (
                "We spotted a big pod of dolphins from the sailboat, then "
                "snorkelled over the reef before a seafood lunch on Wasini "
                "Island - genuinely one of the best days of our whole trip."
            ),
            "de": (
                "Wir haben vom Segelboot aus einen großen Delfinschwarm "
                "gesehen, sind dann über dem Riff geschnorchelt und hatten "
                "anschließend ein Fischmenü auf Wasini Island - wirklich "
                "einer der besten Tage unserer ganzen Reise."
            ),
            "fr": (
                "Nous avons aperçu un grand groupe de dauphins depuis le "
                "voilier, puis fait de la plongée avec tuba au-dessus du "
                "récif avant un déjeuner de fruits de mer sur l'île de "
                "Wasini - vraiment l'une des meilleures journées de tout "
                "notre séjour."
            ),
        },
    },
    {
        "trip_slug": "romantic-canoe-trip",
        "name": "Brian O.",
        "quote": {
            "en": (
                "The sandbank on the canoe trip felt like our own private "
                "beach, and the reef there was in better condition than "
                "anywhere else we snorkelled in Diani."
            ),
            "de": (
                "Die Sandbank bei der Kanutour fühlte sich an wie unser "
                "eigener privater Strand, und das Riff dort war in "
                "besserem Zustand als überall sonst, wo wir in Diani "
                "geschnorchelt sind."
            ),
            "fr": (
                "Le banc de sable de la balade en pirogue avait des airs "
                "de plage privée, et le récif y était en meilleur état que "
                "partout ailleurs où nous avons plongé avec tuba à Diani."
            ),
        },
    },
    {
        "trip_slug": "deep-sea-fishing",
        "name": "Marco T.",
        "quote": {
            "en": (
                "Landed a sailfish on the eight-hour trip and the crew "
                "handled everything - tagging, photos, all of it."
            ),
            "de": (
                "Bei der achtstündigen Tour habe ich einen Segelfisch "
                "gefangen, und die Crew hat sich um alles gekümmert - "
                "Markierung, Fotos, alles."
            ),
            "fr": (
                "J'ai attrapé un voilier lors de la sortie de huit heures, "
                "et l'équipage s'est occupé de tout - le marquage, les "
                "photos, tout."
            ),
        },
    },
    {
        "trip_slug": "jetski-safari",
        "name": "Sofia R.",
        "quote": {
            "en": (
                "Did a 30-minute jet ski ride right after checking in - "
                "the guide took us out through the reef channel and then "
                "let us open up along the coast. Perfect way to start the "
                "holiday."
            ),
            "de": (
                "Direkt nach dem Check-in eine 30-minütige Jetski-Fahrt "
                "gemacht - der Guide hat uns durch den Riffkanal geführt "
                "und uns dann entlang der Küste frei fahren lassen. "
                "Perfekter Urlaubsstart."
            ),
            "fr": (
                "Nous avons fait une balade en jet-ski de 30 minutes juste "
                "après notre arrivée - le guide nous a fait traverser le "
                "chenal du récif avant de nous laisser accélérer le long "
                "de la côte. Un parfait début de vacances."
            ),
        },
    },
]

FAQS = [
    {
        "q": {
            "en": "How far in advance should I book a safari?",
            "de": "Wie weit im Voraus sollte ich eine Safari buchen?",
            "fr": "Combien de temps à l'avance dois-je réserver une excursion ?",
        },
        "a": {
            "en": (
                "For most excursions, 2-3 days' notice is enough. Wild "
                "Fishing in Diani is the exception - boats take a maximum "
                "of 4-6 anglers, so those trips fill up faster. If your "
                "dates are fixed, it's worth booking as soon as you land."
            ),
            "de": (
                "Für die meisten Ausflüge reichen 2-3 Tage Vorlauf. Eine "
                "Ausnahme ist das Hochseeangeln in Diani - die Boote "
                "nehmen maximal 4-6 Angler mit, daher sind diese Touren "
                "schneller ausgebucht. Wenn Ihre Reisetermine feststehen, "
                "lohnt es sich, gleich nach der Ankunft zu buchen."
            ),
            "fr": (
                "Pour la plupart des excursions, 2 à 3 jours de préavis "
                "suffisent. La pêche sportive à Diani fait exception - les "
                "bateaux accueillent au maximum 4 à 6 pêcheurs, ces "
                "sorties se remplissent donc plus vite. Si vos dates sont "
                "fixées, mieux vaut réserver dès votre arrivée."
            ),
        },
    },
    {
        "q": {
            "en": "What happens if the weather doesn't cooperate?",
            "de": "Was passiert, wenn das Wetter nicht mitspielt?",
            "fr": "Que se passe-t-il si la météo n'est pas favorable ?",
        },
        "a": {
            "en": (
                "Guest safety comes first. If our boat crews judge "
                "conditions unsafe, we will reschedule your trip at no "
                "extra cost or refund it in full - your choice."
            ),
            "de": (
                "Die Sicherheit unserer Gäste steht an erster Stelle. Wenn "
                "unsere Bootscrews die Bedingungen als unsicher "
                "einschätzen, verschieben wir Ihre Tour kostenlos oder "
                "erstatten den vollen Betrag - Sie haben die Wahl."
            ),
            "fr": (
                "La sécurité de nos clients passe avant tout. Si nos "
                "équipages jugent les conditions dangereuses, nous "
                "reprogrammerons votre excursion sans frais "
                "supplémentaires ou vous rembourserons intégralement, à "
                "votre choix."
            ),
        },
    },
    {
        "q": {
            "en": "Do you offer hotel pick-up along Diani Beach?",
            "de": "Bieten Sie Abholung von Hotels entlang des Diani Beach an?",
            "fr": "Proposez-vous une prise en charge dans les hôtels le long de Diani Beach ?",
        },
        "a": {
            "en": (
                "Yes, pick-up and drop-off is included on every excursion "
                "on this site. Guests staying on the north coast are "
                "generally collected earlier than those on the south "
                "coast, since the drive to our departure points is longer "
                "- we'll confirm your exact pick-up time when you book."
            ),
            "de": (
                "Ja, Abholung und Rücktransfer sind bei jedem Ausflug auf "
                "dieser Website inbegriffen. Gäste an der Nordküste werden "
                "in der Regel früher abgeholt als Gäste an der Südküste, "
                "da die Anfahrt zu unseren Abfahrtsorten länger dauert - "
                "die genaue Abholzeit bestätigen wir Ihnen bei der "
                "Buchung."
            ),
            "fr": (
                "Oui, la prise en charge et le retour sont inclus pour "
                "chaque excursion sur ce site. Les clients logés sur la "
                "côte nord sont généralement pris en charge plus tôt que "
                "ceux de la côte sud, le trajet jusqu'à nos points de "
                "départ étant plus long - nous vous confirmerons l'heure "
                "exacte lors de la réservation."
            ),
        },
    },
    {
        "q": {
            "en": "Are the excursions suitable for children?",
            "de": "Sind die Ausflüge für Kinder geeignet?",
            "fr": "Les excursions conviennent-elles aux enfants ?",
        },
        "a": {
            "en": (
                "The Glass-Bottom Boat Trip and Wasini Island Day Trip are "
                "family-friendly for most ages. Wild Fishing in Diani "
                "involves a longer day on open water and is better suited "
                "to confident swimmers aged around 10 and up. For the Jet "
                "Ski Safari, riders driving solo are usually expected to "
                "be at least 16, though younger children can ride as a "
                "passenger with an adult."
            ),
            "de": (
                "Die Bootsfahrt mit Glasboden und der Tagesausflug Wasini "
                "Island sind für die meisten Altersgruppen "
                "familienfreundlich. Das Hochseeangeln in Diani bedeutet "
                "einen längeren Tag auf offenem Wasser und eignet sich "
                "besser für sichere Schwimmer ab etwa 10 Jahren. Bei der "
                "Jetski-Safari müssen Fahrer, die allein fahren, in der "
                "Regel mindestens 16 Jahre alt sein, jüngere Kinder können "
                "jedoch als Beifahrer mit einem Erwachsenen mitfahren."
            ),
            "fr": (
                "La sortie en bateau à fond de verre et l'excursion à "
                "l'île de Wasini conviennent à la plupart des âges. La "
                "pêche sportive à Diani implique une journée plus longue "
                "en pleine mer et convient mieux aux nageurs confiants à "
                "partir d'environ 10 ans. Pour le safari en jet-ski, les "
                "conducteurs en solo doivent généralement avoir au moins "
                "16 ans, mais les enfants plus jeunes peuvent monter en "
                "tant que passagers avec un adulte."
            ),
        },
    },
    {
        "q": {
            "en": "Do I need to know how to swim?",
            "de": "Muss ich schwimmen können?",
            "fr": "Dois-je savoir nager ?",
        },
        "a": {
            "en": (
                "For our snorkeling-based trips, basic swimming confidence "
                "in open water is recommended, though life jackets are "
                "provided throughout. Non-swimmers are welcome on the "
                "Glass-Bottom Boat Trip in particular, since you can see "
                "the reef through the glass panel without getting in the "
                "water."
            ),
            "de": (
                "Für unsere Schnorchel-Ausflüge wird grundlegende "
                "Schwimmsicherheit im offenen Wasser empfohlen, "
                "Schwimmwesten werden jedoch durchgehend gestellt. "
                "Nichtschwimmer sind besonders bei der Bootsfahrt mit "
                "Glasboden willkommen, da Sie das Riff durch die "
                "Glasscheibe sehen können, ohne ins Wasser zu müssen."
            ),
            "fr": (
                "Pour nos excursions avec plongée avec tuba, une aisance "
                "de base en eau libre est recommandée, bien que des "
                "gilets de sauvetage soient fournis tout au long. Les "
                "non-nageurs sont particulièrement les bienvenus sur la "
                "sortie en bateau à fond de verre, puisque vous pouvez "
                "observer le récif à travers la vitre sans avoir à entrer "
                "dans l'eau."
            ),
        },
    },
]

CONTACT_INFO = {
    "phone": "+254 103 928 036",
    "whatsapp": "+254 103 928 036",
    "email": "dianiseaadventures@gmail.com",
    "address": "Diani Beach Road, Diani Beach, Kwale County, Kenya",
    "hours": [
        {
            "day": {
                "en": "Monday - Saturday",
                "de": "Montag - Samstag",
                "fr": "Lundi - Samedi",
            },
            "time": "6:00am - 7:00pm",
        },
        {
            "day": {"en": "Sunday", "de": "Sonntag", "fr": "Dimanche"},
            "time": "6:00am - 5:00pm",
        },
    ],
}

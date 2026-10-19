"""
Seeds the key_makers table with 10 FICTIONAL featured founders for the demo.

Every business, person, quote and story below is invented sample data —
this portfolio copy contains no real client information. Four entries
include full bio content (title/location/industry/key_quotes/story); the
other six leave those fields unset, which the Profiles page renders as
"Bio pending". key_quotes is stored as a JSON string (json.dumps of a
list[str]) — see KeyMaker.key_quotes' docstring in app/models/content.py.

Run manually against a provisioned database:
    cd backend && python seed_key_makers_public.py
"""

import json

from app.database import SessionLocal
from app.models import KeyMaker

KEY_MAKERS = [
    {
        "business_name": "Maple & Rye Bakehouse",
        "owner_name": "Dana Whitfield",
        "business_type": "Bakery / Catering",
        "website": "https://example.com/maple-rye",
        "social_media": "Instagram: https://example.com/maple_rye",
        "photo_url": None,
        "title": "Founder",
        "location": "Riverside, Example City",
        "industry": "Food / Culinary / Hospitality",
        "key_quotes": json.dumps(
            [
                "If you have the will to do what's in your heart, you can do it. "
                "It doesn't matter where you start."
            ]
        ),
        "story": (
            "Dana Whitfield, founder of Maple & Rye Bakehouse, started her business because she "
            "wanted to build something of her own. She didn't know where the journey would lead, "
            "but she held onto one thing throughout: persistence.\n\n"
            "Her recipes come from her grandmother's kitchen, and the bakehouse has become a "
            "neighborhood gathering place. Over time she stopped seeing setbacks as obstacles and "
            "began treating them as lessons.\n\n"
            "Core story/theme: Dana turned a desire to build something of her own into a "
            "purpose-driven business rooted in family and community.\n\n"
            "Key message: Where you start doesn't determine what you can build."
        ),
    },
    {
        "business_name": "Northside Movement Studio",
        "owner_name": "Priya Raman",
        "business_type": "Dance Education",
        "website": "https://example.com/northside-movement",
        "social_media": "Instagram: https://example.com/northside_movement",
        "photo_url": None,
        "title": "Owner & Lead Instructor",
        "location": "Northside, Example City",
        "industry": "Dance education / Arts / Youth development",
        "key_quotes": json.dumps(
            [
                "I opened the studio because our neighborhood had no arts programs for young "
                "people to express themselves.",
                "It's an honor that families see it as a safe place.",
            ]
        ),
        "story": (
            "Priya Raman founded Northside Movement Studio after noticing a gap in arts education "
            "in her community. After years teaching dance in schools, she wanted a place where "
            "young people could build skills, find mentorship, and feel supported.\n\n"
            "Building the studio took patience. Some weeks had only a few students, and she "
            "learned to run a business as she went. Today, students who first came as middle "
            "schoolers now bring their own children.\n\n"
            "Core story/theme: a lack of arts opportunities became a long-term community "
            "institution connecting generations."
        ),
    },
    {
        "business_name": "Bloom Street Salon",
        "owner_name": "Marisol Vega",
        "business_type": "Beauty Salon",
        "website": None,
        "social_media": None,
        "photo_url": None,
        "industry": "Beauty and personal care",
        "key_quotes": json.dumps(
            [
                "I learned about the loan, which helped me pave the way to my second salon.",
                "You always start from below, and if you are strong, you can do it.",
            ]
        ),
        "story": (
            "Marisol's entrepreneurial journey began with inspiration from her sister, who already "
            "had a business. With her partner's encouragement she opened her first salon.\n\n"
            "A turning point came when she learned about small-business loans. Financing gave her "
            "the resources and confidence to open a second location, and she hopes the women who "
            "work alongside her will one day open businesses of their own.\n\n"
            "Key message: Never think it's too late to start."
        ),
    },
    {
        "business_name": "QuickStop Financial Services",
        "owner_name": "Frank Dellarosa",
        "business_type": "Financial Services",
        "website": "https://example.com/quickstop",
        "social_media": None,
        "photo_url": None,
    },
    {
        "business_name": "Hearth & Cradle Postnatal Care",
        "owner_name": "Amara Okafor",
        "business_type": "Postpartum Care",
        "website": "https://example.com/hearth-cradle",
        "social_media": "Instagram: https://example.com/hearth_cradle",
        "photo_url": None,
    },
    {
        "business_name": "Island Breeze Kitchen",
        "owner_name": "Simone Laurent",
        "business_type": "Food / Bakery",
        "website": "https://example.com/island-breeze",
        "social_media": "Instagram: https://example.com/island_breeze",
        "photo_url": None,
    },
    {
        "business_name": "Paper Moon Studio",
        "owner_name": "Marta Quinn",
        "business_type": "Art / Home Décor / Gifts",
        "website": "https://example.com/paper-moon",
        "social_media": "Instagram: https://example.com/paper_moon",
        "photo_url": None,
    },
    {
        "business_name": "Greenleaf Wellness Shop",
        "owner_name": "Gloria Santos",
        "business_type": "Wellness Retail Shop",
        "website": None,
        "social_media": "Instagram: https://example.com/greenleaf_wellness",
        "photo_url": None,
    },
    {
        "business_name": "Polished Lounge",
        "owner_name": "Gwen Alvarez",
        "business_type": "Nail / Beauty Services",
        "website": None,
        "social_media": "Instagram: https://example.com/polished_lounge",
        "photo_url": None,
    },
    {
        "business_name": "Stitched With Love Creations",
        "owner_name": "Yolanda Price",
        "business_type": "Custom Inspirational Gifts",
        "website": "https://example.com/stitched-with-love",
        "social_media": "Instagram: https://example.com/stitched_with_love",
        "photo_url": None,
        "industry": "Creative arts / Inspirational products / Handmade creations",
        "key_quotes": json.dumps(
            [
                "I wanted to create something meaningful, uplifting, and comforting.",
                "My uniqueness is my audience.",
            ]
        ),
        "story": (
            "Yolanda Price created Stitched With Love Creations to make something more than a "
            "product: pieces that connect with people on a deeper level.\n\n"
            "Her biggest challenge was finding the right audience. After a slow day with a single "
            "customer who told her the work was beautiful and unique, she realized she didn't need "
            "to appeal to everyone, only to the people who valued what she made.\n\n"
            "Core story/theme: embracing uniqueness rather than fitting someone else's mold."
        ),
    },
]


def seed():
    db = SessionLocal()
    try:
        existing = {km.business_name for km in db.query(KeyMaker).all()}
        added = 0
        for entry in KEY_MAKERS:
            if entry["business_name"] in existing:
                continue
            db.add(KeyMaker(**entry))
            added += 1
        db.commit()
        print(f"Seeded {added} new Key Makers ({len(KEY_MAKERS) - added} already present).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()

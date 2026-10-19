"""
Harbor Light Fund X (Twitter) — Sample Post Templates

FICTIONAL sample posts for a fictional organization, written to mirror the
short-caption style of a small-business nonprofit's X feed. Used as "Fixed
template" starting points on the event-form page — staff pick one and
use/edit it directly, with no AI call involved. Distinct from AI Copy
generation (app/services/prompts.py's "x" SOCIAL_POST_VARIANTS entry).

All names, dates and links below are invented placeholders.
"""

X_TEMPLATES: dict[str, dict] = {
    "september_events_carousel": {
        "label": "Event promo — carousel, 3 upcoming events",
        "category": "event_promo",
        "caption": """Meet Harbor Light Fund this fall: Founders Investment Suite 9/20, Cash Flow Workshop 9/23, and the Regional Business Conference 9/29.

example.com/events/""",
        "hashtags": ["#HLF", "#LocalEntrepreneurs"],
    },
    "next_chapter_loan_inquiry": {
        "label": "Evergreen — loan inquiry CTA, no event date",
        "category": "evergreen",
        "caption": """Your Business Deserves a Next Chapter. ❤️

You believed in your business. So do we. Ready to grow?

Harbor Light Fund wants to hear from women entrepreneurs with established businesses and a vision for what's next.

👉 Start your Loan Inquiry: example.com/loan-inquiry""",
        "hashtags": ["#loanapps", "#smallbiz"],
    },
    "government_contracting": {
        "label": "Event promo — certification / government contracting webinar",
        "category": "event_promo",
        "caption": """🚨 Don't Leave Money on the Table!
Learn how business certification opens the door to government contracts.

📅 June 10 | ⏰ 12PM–1PM | 💻 Zoom
Register: example.com/events/contracting""",
        "hashtags": ["#SmallBiz"],
    },
    "legal_help_10_spots": {
        "label": "Event promo — urgency/limited-spots framing",
        "category": "event_promo",
        "caption": """🚨 ONLY 10 SPOTS LEFT 🚨

FREE one-on-one legal consultations with volunteer attorneys: contracts, leases, business structure and more.

📅 April 24 | ⏰ 3:30–5:45 PM | 📍 In person
Apply: example.com/events/legal""",
        "hashtags": [],
    },
    "lunch_and_apply_funding": {
        "label": "Event promo — recurring virtual session",
        "category": "event_promo",
        "caption": """✨ WE'RE FUNDING — ARE YOU READY? ✨

Join our virtual Lunch & APPLY sessions and learn how to position your business for funding and growth.

📅 May 14 | June 11 | July 9 • ⏰ 12PM ET • 💻 Zoom
Register: example.com/events/lunch-and-apply""",
        "hashtags": ["#HLF", "#WomenEntrepreneurs"],
    },
    "money_matters_cash_flow": {
        "label": "Event promo — workshop with learning checklist",
        "category": "event_promo",
        "caption": """💰 Strong businesses know their numbers.

Join our Small Business Month workshop: cash flow, profit & loss, budgeting for growth and funding readiness.

📅 May 20 • ⏰ 11AM • 💻 Zoom
example.com/events/money-matters""",
        "hashtags": ["#SmallBusinessMonth", "#MoneyMatters"],
    },
    "ai_marketing_webinar_today": {
        "label": "Event promo — happening-today reminder",
        "category": "event_promo",
        "caption": """🚨 HAPPENING TODAY at 11 AM 🚨

Learn how AI tools can simplify and scale your marketing — content, emails and social posts in minutes, not hours.

👉 Register: example.com/events/ai-marketing""",
        "hashtags": ["#AIforBusiness"],
    },
    "financial_literacy_poll_know_your_numbers": {
        "label": "Engagement post — poll prompt, no event",
        "category": "engagement",
        "caption": """Be honest: how often do you check your business finances?

A) Weekly
B) Monthly
C) When I'm stressed

Reply with your letter, no judgment! 👇""",
        "hashtags": ["#FinancialLiteracyMonth", "#EntrepreneurLife"],
    },
    "financial_literacy_month_awareness": {
        "label": "Awareness post — monthly theme framing",
        "category": "awareness",
        "caption": """April is Financial Literacy Month!

Strong businesses = strong financial foundations: cash flow, credit, capital access.

We're here to help you build, grow and fund your business with confidence.""",
        "hashtags": ["#FinancialLiteracyMonth", "#AccessToCapital"],
    },
}


def list_x_templates() -> dict[str, str]:
    """Returns {template_key: label} for every sample X template — for
    populating a frontend picker, same pattern as
    instagram_templates.list_instagram_templates()."""
    return {key: t["label"] for key, t in X_TEMPLATES.items()}


def get_x_template(template_key: str) -> dict:
    """
    Returns one X template's full data (label, category, caption,
    hashtags). Raises KeyError with the valid options listed if
    template_key is unrecognized, matching
    instagram_templates.get_instagram_template()'s error shape.
    """
    template = X_TEMPLATES.get(template_key)
    if template is None:
        raise KeyError(
            f"Unknown X template '{template_key}'. Valid options: "
            f"{list(X_TEMPLATES.keys())}"
        )
    return template

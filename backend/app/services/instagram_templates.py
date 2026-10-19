"""
Harbor Light Fund Instagram — Sample Post Templates

FICTIONAL sample posts for a fictional organization, written to mirror the
structural patterns of a real small-business nonprofit's Instagram feed
(emoji-marker checklists, urgency framing, quote cards, polls). Used as
"Fixed template" starting points on the event-form page — staff pick one and
use/edit it directly, with no AI call involved. Distinct from AI Copy
generation (app/services/prompts.py's "instagram" SOCIAL_POST_VARIANTS
entry), which generates a NEW caption grounded in the same observed style
rather than reusing one verbatim.

All names, dates and links below are invented placeholders.
"""

INSTAGRAM_TEMPLATES: dict[str, dict] = {
    "credit_building_webinar": {
        "label": "Event promo — checklist + emoji markers",
        "category": "event_promo",
        "caption": """Ready to make next year your year? Start building your credit today!

If your credit isn't where you want it to be, don't wait. Learn practical strategies to build, repair, and strengthen your credit so you're ready for future financing opportunities.

📅 Wednesday, March 12
🕐 12:00–1:00 PM

🎯 Your financial future starts now. Don't miss this FREE webinar!

👉 Register now: https://example.com/register/credit-webinar""",
        "hashtags": [
            "#HarborLightFund",
            "#CreditBuilding",
            "#LoanReady",
            "#SmallBusiness",
            "#WomenEntrepreneurs",
        ],
    },
    "legal_help_urgency": {
        "label": "Event promo — urgency/limited-spots framing",
        "category": "event_promo",
        "caption": """🚨 ONLY 10 SPOTS LEFT 🚨

Need legal help for your business?

Harbor Light Fund and the Community Legal Clinic are offering FREE one-on-one consultations with volunteer attorneys.

Get answers to your questions about:
✔ Business Structure
✔ Contracts
✔ Commercial Leases
✔ Intellectual Property
✔ Legal Issues Affecting Your Business

📅 April 24
⏰ 3:30 PM – 5:45 PM
📍 In-Person Session
💥 FREE 40-minute consultation 💥 Limited availability 💥 Approved applicants only

⚠️ Spots are filling quickly. Don't wait until it's too late.""",
        "hashtags": [],
        "truncated": True,
    },
    "funding_lunch_apply": {
        "label": "Event promo — sparkle hook + emoji bullet list",
        "category": "event_promo",
        "caption": """✨ WE'RE FUNDING — ARE YOU READY? ✨

Women entrepreneurs, this is your sign to stop waiting and start growing. 🚀

Join Harbor Light Fund for our virtual Lunch & APPLY sessions where you'll learn how to confidently position your business for funding and growth.

💡 Perfect for businesses ready for:
💰 Working Capital
🏢 Second Locations
📦 Additional Product Lines
📢 Targeted Digital Marketing Campaigns
📈 Increased Revenue Growth

📅 May 14 | June 11 | July 9
⏰ 12PM–1PM ET
💻 Zoom

👤 Hosted by Jordan Ellis, Director of Harbor Light Fund

🥗 Bring your lunch
💻 Bring your laptop
🔥 Bring your business goals

🔗 Register here: https://example.com/register/lunch-and-apply""",
        "hashtags": [
            "#HLF",
            "#HarborLightFund",
            "#WomenOwnedBusiness",
            "#WomenEntrepreneurs",
            "#FundingAndTraining",
        ],
    },
    "money_matters_workshop": {
        "label": "Event promo — checklist + \"strong businesses\" close",
        "category": "event_promo",
        "caption": """💰 READY TO GET FUNDING READY?

This Small Business Month, join Harbor Light Fund & the Regional Business Alliance for a powerful financial workshop designed for entrepreneurs ready to grow smarter.

📊 Learn:
✔ Cash Flow Management
✔ Understanding Profit & Loss
✔ Budgeting for Growth
✔ Funding Readiness Tips

📅 May 20
⏰ 11AM – 12PM
💻 Zoom Webinar

🔥 Strong businesses know their numbers.
🔥 Smart entrepreneurs prepare for capital.

📮 Register now through the link:
https://example.com/register/money-matters""",
        "hashtags": [
            "#SmallBusinessMonth",
            "#HLFEntrepreneurs",
            "#MoneyMatters",
            "#BusinessGrowth",
            "#FinancialEducation",
        ],
    },
    "ai_marketing_webinar_reminder": {
        "label": "Event promo — happening-today reminder, AI/marketing topic",
        "category": "event_promo",
        "caption": """🚨 HAPPENING TODAY at 11 AM (1 Hour Only!) 🚨

Entrepreneurs—this is your moment to stop overworking your marketing and start working smarter.

Join Harbor Light Fund for a power-packed LIVE Zoom training on using AI tools to simplify and scale your marketing.

💡 Imagine creating content, emails, and social posts in minutes—not hours.
💡 Imagine automating your marketing while increasing visibility.

That's exactly what you'll learn today with guest expert Sam Rivera (Brightside Marketing Co.).

🔥 What you'll walk away with:
• AI tools you can start using TODAY
• Faster content creation strategies
• Smarter marketing systems that save time
• Real tactics to boost engagement + growth

⏰ 11AM – Don't miss it. This is your last call.
👉 Register now: https://example.com/register/ai-marketing""",
        "hashtags": [],
    },
    "ai_marketing_webinar_announcement": {
        "label": "Event promo — lightning-bolt hook, full detail version",
        "category": "event_promo",
        "caption": """⚡ STOP doing everything manually ⚡

This Financial Literacy Month, learn how to WORK SMARTER.

Join Harbor Light Fund for a webinar on using AI to simplify your marketing and grow your business 🔥

✨ You'll learn how to:
• Create content in minutes
• Automate your marketing
• Build a stronger brand
• Save HOURS every week

🧑‍💼 Perfect for entrepreneurs ready to level up

📅 April 30
⏰ 12PM – 1PM
💻 Live Webinar

🚨 Don't miss learning during Financial Literacy Month, this is a game changer.
👉 Register now: https://example.com/register/ai-marketing""",
        "hashtags": [
            "#HLFFinancialLiteracyMonth",
            "#BossWomen",
            "#EntrepreneurLife",
            "#MarketingTips",
            "#AIforBusiness",
            "#HLF",
        ],
    },
    "financial_literacy_month_intro": {
        "label": "Awareness post — no event, monthly theme framing",
        "category": "awareness",
        "caption": """April is Financial Literacy Month!

Strong businesses = strong financial foundations 👍
✔ Cash Flow
✔ Credit
✔ Capital Access

Harbor Light Fund is here to help you build, grow, and fund your business with confidence.

Don't wait, start strengthening your business today.

Register: https://example.com/register/financial-literacy""",
        "hashtags": [
            "#FinancialLiteracyMonth",
            "#WomenInBusiness",
            "#SmallBizTips",
            "#LocalEntrepreneurs",
            "#BusinessGrowth",
            "#AccessToCapital",
        ],
    },
    "money_finances_poll": {
        "label": "Engagement post — poll/comment prompt, no event",
        "category": "engagement",
        "caption": """🚩 Entrepreneurs: Stop Guessing With Your Business Finances 🚩

Your business may be making sales... but do you truly understand your numbers? 👀💰

This Small Business Month, Harbor Light Fund and the Regional Business Alliance are bringing entrepreneurs together for a powerful conversation on the financial side of business growth.

📌 If you want funding, lenders want to see that you understand:
✔ Cash Flow""",
        "hashtags": [],
    },
    "tribe_of_women_quote": {
        "label": "Quote card — inspirational, minimal caption",
        "category": "quote",
        "caption": """Behind every successful woman is a tribe of other successful women who have her back""",
        "hashtags": [],
    },
    "money_moves_poll": {
        "label": "Engagement post — A/B/C poll, comment-bait CTA",
        "category": "engagement",
        "caption": """Be honest...

Do you check your business finances...
A) Weekly
B) Monthly
C) When you're stressed

It's Financial Literacy Month, so let's tighten up!

Money Moves to Make NOW:
Know your cash flow (don't guess)
Separate your accounts
Check your P&L like your IG insights
Track expenses yes, even that $9.99
Build business credit BEFORE you need it

Harbor Light Fund is here to help you get funded + stay ready 💪

👍 Comment A, B, or C - no judgment!""",
        "hashtags": [
            "#FinancialLiteracyMonth",
            "#MoneyTalk",
            "#EntrepreneurLife",
            "#WomenInBusiness",
            "#SmallBusinessTips",
            "#HLF",
        ],
    },
}


def list_instagram_templates() -> dict[str, str]:
    """Returns {template_key: label} for every sample Instagram template —
    for populating a frontend picker, same pattern as
    keymakers_campaign.list_keymakers_stages()."""
    return {key: t["label"] for key, t in INSTAGRAM_TEMPLATES.items()}


def get_instagram_template(template_key: str) -> dict:
    """
    Returns one Instagram template's full data (label, category, caption,
    hashtags). Raises KeyError with the valid options listed if
    template_key is unrecognized, matching
    keymakers_campaign.get_keymakers_stage()'s error shape.
    """
    template = INSTAGRAM_TEMPLATES.get(template_key)
    if template is None:
        raise KeyError(
            f"Unknown Instagram template '{template_key}'. Valid options: "
            f"{list(INSTAGRAM_TEMPLATES.keys())}"
        )
    return template

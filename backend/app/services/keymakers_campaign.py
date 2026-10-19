"""
Harbor Light Fund "Trailblazers" Campaign — Sample Reference Copy

FICTIONAL sample copy for a fictional recruitment campaign. The
"Trailblazers" initiative invites past and prospective clients of the
(fictional) Harbor Light Fund to record short video testimonials answering
"What was your spark?" — the person, decision, resource, or turning point
that changed what was possible for their business. Selected stories feed the
Member Spotlight newsletter block (see newsletter_blocks.py /
build_member_spotlight_prompt).

Two audience variants exist — "Current Clients" and "Cold List of
Entrepreneurs". The sequence is a 4-email drip (initial invite + follow-ups
at day 4/9/15). This is a *reference* for tone/structure, not send-ready
copy.

Deliberately NOT merged into brand_voice.py's EXAMPLE_POSTS — those are
evergreen, always-injected brand voice; this is a specific, time-bound
campaign with its own sequencing rules. Exposed as its own context function
so callers opt in explicitly rather than it silently influencing every
generation call.

(Identifiers keep the original "keymakers" naming so the API surface and
database tables are unchanged.)
"""

KEYMAKERS_SEQUENCE_CURRENT_CLIENTS = [
    {
        "stage": "initial",
        "send_day": 0,
        "subject_options": None,
        "body": """Hello [First Name],
Every business has a moment when something shifted.
[TRAILBLAZERS VISUAL]
Harbor Light Fund is launching Trailblazers, a community that celebrates the women entrepreneurs who made it happen and helps the next generation follow.
As part of the Harbor Light community, we'd love for you to answer one simple question:
What was your spark?
The person, decision, resource, or turning point that changed what was possible for your business.
We'd like to capture your answer in a brief recorded conversation. Your story could help another woman take her next step with confidence.
[SHARE YOUR SPARK]
Recording isn't the only way to take part. You can also nominate another entrepreneur, attend our fall gathering, or join the growing Trailblazers community.
[VISIT TRAILBLAZERS]
Warmly,
Alex Morgan
Founder and President
Harbor Light Fund""",
    },
    {
        "stage": "follow_up_1",
        "send_day": 4,
        "send_condition": "Only to contacts who did not reply, did not complete the form, did not opt out, and did not bounce.",
        "subject_options": [
            "What was the spark for your business?",
            "We'd like to include your story",
            "A quick Trailblazers follow-up",
        ],
        "body": """Hello [First Name],
We're following up on our recent invitation because we'd truly love to hear your story.
Every entrepreneur has a moment that moved their business forward. We call that your spark.
What was your spark?
It's a brief, guided conversation with nothing to prepare.
[SHARE YOUR SPARK]
Your story could encourage and open doors for other women entrepreneurs.
[VISIT TRAILBLAZERS]
We hope you'll join us.
Warmly,
Alex Morgan
Founder and President
Harbor Light Fund""",
    },
    {
        "stage": "follow_up_2",
        "send_day": 9,
        "send_condition": (
            "Offer a different reason to participate — emphasize one of: their experience "
            "may help another entrepreneur; selected stories will join the first collection; "
            "no speech or preparation is required; there are other ways to participate."
        ),
        "subject_options": [
            "Another entrepreneur may need what you learned",
            "Your experience belongs in Trailblazers",
            "The lessons behind the business",
        ],
        "body": """Hello [First Name],
Every founder learns lessons you can't find in a book.
Sometimes it's the introduction that led to a first customer. Sometimes it's the mistake that became the best teacher.
By sharing your story in a short conversation, you can help someone else avoid a costly mistake or take a leap with more confidence.
[SHARE YOUR SPARK]
If recording isn't the right fit, you can nominate another woman entrepreneur or stay connected as Trailblazers grows.
[VISIT TRAILBLAZERS]
Thank you for helping build a community where women learn from one another.
Warmly,
Alex Morgan
Founder and President
Harbor Light Fund""",
    },
    {
        "stage": "final_follow_up",
        "send_day": 15,
        "send_condition": (
            "Brief closing message. Do not use false urgency — explain that the first "
            "group of interviews is being completed."
        ),
        "subject_options": [
            "Final invitation for the first Trailblazers collection",
            "We hope your story will be included",
            "One last Trailblazers invitation",
        ],
        "body": """Hello [First Name],
As we prepare the first Trailblazers collection, we wanted to extend one final invitation.
Every business has a story behind it. We'd be honored to include yours.
[SHARE YOUR SPARK]
If now isn't the right time, you can still take part by nominating another entrepreneur.
[VISIT TRAILBLAZERS]
Thank you for being part of the Harbor Light Fund community.
Warmly,
Alex Morgan
Founder and President
Harbor Light Fund""",
    },
]

KEYMAKERS_SEQUENCE_COLD_LIST = [
    {
        "stage": "initial",
        "send_day": 0,
        "subject_options": None,
        "body": """Hello [First Name],
Women entrepreneurs hear plenty of success stories. What they rarely hear is what actually made the difference.
The introduction that led to a major customer. The financing that arrived at the right moment. The decision that changed the course of the business.
Harbor Light Fund is building Trailblazers, a community where women share the stories, knowledge and relationships that move businesses forward.
We are beginning with one question:
What was your spark?
We'd love to hear your answer in a brief, guided recorded conversation. No preparation is required.
[SHARE YOUR SPARK]
For over twenty years, Harbor Light Fund has worked alongside women entrepreneurs by providing financing, practical guidance and business connections.
[Learn more about Harbor Light Fund.]
You can also nominate another woman whose story should be heard or join us at the fall gathering.
[VISIT TRAILBLAZERS]
We are now selecting the first group of stories. We hope yours will be one of them.
Warmly,
Alex Morgan
Founder and President
Harbor Light Fund""",
    },
]
# Only the initial-touch cold-list message exists as sample copy; reuse the
# Current Clients follow-up structure/timing if a cold-list drip is needed.


# Stable, dropdown-friendly registry of every individual message, keyed by
# a single stage_key — this is what the newsletter generator's campaign
# toggle selects from (one message per generation call, not the whole
# sequence at once). "label" is what a frontend dropdown should show.
KEYMAKERS_STAGES: dict[str, dict] = {
    "current_clients_initial": {
        "label": "Initial invite — Current Clients",
        "audience": "Current Clients",
        **KEYMAKERS_SEQUENCE_CURRENT_CLIENTS[0],
    },
    "current_clients_follow_up_1": {
        "label": "Day 4 follow-up — Current Clients",
        "audience": "Current Clients",
        **KEYMAKERS_SEQUENCE_CURRENT_CLIENTS[1],
    },
    "current_clients_follow_up_2": {
        "label": "Day 9 follow-up — Current Clients",
        "audience": "Current Clients",
        **KEYMAKERS_SEQUENCE_CURRENT_CLIENTS[2],
    },
    "current_clients_final_follow_up": {
        "label": "Day 15 final follow-up — Current Clients",
        "audience": "Current Clients",
        **KEYMAKERS_SEQUENCE_CURRENT_CLIENTS[3],
    },
    "cold_list_initial": {
        "label": "Initial invite — Cold List of Entrepreneurs",
        "audience": "Cold List of Entrepreneurs",
        **KEYMAKERS_SEQUENCE_COLD_LIST[0],
    },
}

KEYMAKERS_CENTRAL_QUESTION = "What was your spark?"
KEYMAKERS_CENTRAL_QUESTION_SUBTEXT = (
    "The person, decision, resource, or turning point that "
    "changed what was possible for your business."
)

KEYMAKERS_APPROVAL_NOTE = (
    "All Trailblazers messages require approval before sending — "
    "this reference copy is for tone/structure, not send-ready output."
)


def get_keymakers_campaign_context() -> str:
    """
    Returns the Trailblazers recruitment campaign as a string for prompt
    injection — for generating campaign-specific content (e.g. an eblast
    inviting founders to share their story), not for general brand voice.
    Callers opt in explicitly; this is not part of get_brand_voice_context().
    """
    current_clients_str = "\n\n---\n\n".join(
        f"**{msg['stage']} (day {msg['send_day']})**"
        + (f"\nSubject options: {', '.join(msg['subject_options'])}" if msg.get("subject_options") else "")
        + f"\n\n{msg['body']}"
        for msg in KEYMAKERS_SEQUENCE_CURRENT_CLIENTS
    )

    return f"""
# Harbor Light Fund Trailblazers Recruitment Campaign (reference)

## Central Question
{KEYMAKERS_CENTRAL_QUESTION}
{KEYMAKERS_CENTRAL_QUESTION_SUBTEXT}

## Approval
{KEYMAKERS_APPROVAL_NOTE}

## Current-Clients Sequence (4 messages: initial + follow-ups at day 4, 9, 15)
{current_clients_str}
"""


def list_keymakers_stages() -> dict[str, str]:
    """Returns {stage_key: label} for every individual campaign message —
    for populating a frontend dropdown, same pattern as
    prompts.list_variants()."""
    return {key: stage["label"] for key, stage in KEYMAKERS_STAGES.items()}


def get_keymakers_stage(stage_key: str) -> dict:
    """
    Returns ONE campaign stage as structured data (label, audience, stage,
    send_day, subject_options, body) — for a frontend that wants to render
    the reference copy directly (e.g. a static-template preview), rather
    than get_keymakers_stage_context()'s formatted prompt-injection string.
    Raises KeyError with the valid options listed if stage_key is
    unrecognized, matching get_keymakers_stage_context()'s error shape.
    """
    stage = KEYMAKERS_STAGES.get(stage_key)
    if stage is None:
        raise KeyError(
            f"Unknown Keymakers stage '{stage_key}'. Valid options: "
            f"{list(KEYMAKERS_STAGES.keys())}"
        )
    return stage


def get_keymakers_stage_context(stage_key: str) -> str:
    """
    Returns ONE selected campaign message as prompt-injection context —
    the reference copy for a single stage (e.g. "current_clients_initial"),
    not the whole sequence. Raises KeyError with the valid options listed
    if stage_key is unrecognized, so callers get an actionable error
    instead of a silent empty prompt.
    """
    stage = KEYMAKERS_STAGES.get(stage_key)
    if stage is None:
        raise KeyError(
            f"Unknown Keymakers stage '{stage_key}'. Valid options: "
            f"{list(KEYMAKERS_STAGES.keys())}"
        )

    subject_line = (
        f"\nSubject options: {', '.join(stage['subject_options'])}"
        if stage.get("subject_options")
        else ""
    )
    send_condition = (
        f"\nSend condition: {stage['send_condition']}" if stage.get("send_condition") else ""
    )

    return f"""
# Harbor Light Fund Trailblazers Recruitment Campaign — Reference Message

## Central Question
{KEYMAKERS_CENTRAL_QUESTION}
{KEYMAKERS_CENTRAL_QUESTION_SUBTEXT}

## Approval
{KEYMAKERS_APPROVAL_NOTE}

## Selected Stage: {stage['label']}
Audience: {stage['audience']} | Stage: {stage['stage']} (day {stage['send_day']}){subject_line}{send_condition}

## Reference Copy
{stage['body']}
"""

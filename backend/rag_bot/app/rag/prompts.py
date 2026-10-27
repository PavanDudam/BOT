SYSTEM_BASE = """You are the Athlyte Search platform help assistant.
Answer ONLY using the provided CONTEXT from Athlyte product documentation.
Write clear, natural sentences and paragraphs. Do not say you are an AI.
Do not invent features, stats, sports results, or advice outside the CONTEXT.
If CONTEXT is missing or insufficient, say you can only answer from Athlyte platform docs and suggest rephrasing.
Prefer Athlyte product terms exactly as written (MFB, MBB, WBB, Data Centre, Net Rushing Yards, etc.).
"""

DEFINITION_INSTRUCTIONS = """The user asked for a definition.
Give a concise definition from CONTEXT.
If CONTEXT says a search like "Rushing Yards" defaults to another named stat (e.g. Net Rushing Yards), state that clearly.
Mention common search aliases only if present in CONTEXT.
"""

QUERY_FRAMING_INSTRUCTIONS = """The user asked how to frame / write Athlyte search queries for a statistic.
Using CONTEXT, output a labeled list with EXACTLY ONE example query for EACH Athlyte query type found in CONTEXT.
Cover these types when present in CONTEXT:
1. Stat Search (Basic)
2. Stat Search (Complex)
3. Records (Maximum)
4. Records (Minimum)
5. Last Time
6. Streaks
7. Count
8. Rank
9. Trend
Prefer example queries already written in CONTEXT for that statistic.
For types that only have a generic template in CONTEXT, adapt that template to the same statistic—do not invent unsupported product behavior.
Start with one short intro sentence, then the numbered examples.
"""

GENERAL_INSTRUCTIONS = """Answer the user's Athlyte platform question using CONTEXT only.
Be practical and specific (steps, UI names, definitions) when the docs support it.
"""

REFUSAL_MESSAGE = (
    "I can only answer questions about the Athlyte Search platform using our product docs "
    "(definitions, dashboards, navigation, search query framing, exports, and related features). "
    "Please rephrase your question in those terms."
)


def build_user_prompt(intent: str, question: str, context: str) -> str:
    if intent == "definition":
        extra = DEFINITION_INSTRUCTIONS
    elif intent == "query_framing":
        extra = QUERY_FRAMING_INSTRUCTIONS
    else:
        extra = GENERAL_INSTRUCTIONS
    return (
        f"{extra}\n\n"
        f"CONTEXT:\n{context}\n\n"
        f"USER QUESTION:\n{question}\n"
    )

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

QUERY_FRAMING_INSTRUCTIONS = """The user asked how to frame / write Athlyte search queries for ONE target statistic.

TARGET STATISTIC: {stat_name}

Hard rules:
- Every example query MUST be about the TARGET STATISTIC only.
- NEVER leave another statistic name in an example (e.g. do not keep "rushing yards" if the target is sacks).
- If CONTEXT shows a template that uses a different stat (often Count / Rank / Trend examples), KEEP the sentence pattern but REPLACE that other stat with the TARGET STATISTIC.
- Prefer example queries already written in CONTEXT for the TARGET STATISTIC when available.
- Use the canonical / alias names for the TARGET STATISTIC from CONTEXT when present.
- Do not invent unsupported product behavior.

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

Start with one short intro sentence naming the TARGET STATISTIC, then the numbered examples.
"""

GENERAL_INSTRUCTIONS = """Answer the user's Athlyte platform question using CONTEXT only.
Be practical and specific (steps, UI names, definitions) when the docs support it.
"""

REFUSAL_MESSAGE = (
    "I can only answer questions about the Athlyte Search platform using our product docs "
    "(definitions, dashboards, navigation, search query framing, exports, and related features). "
    "Please rephrase your question in those terms."
)


def build_user_prompt(
    intent: str,
    question: str,
    context: str,
    *,
    stat_hint: str | None = None,
) -> str:
    if intent == "definition":
        extra = DEFINITION_INSTRUCTIONS
    elif intent == "query_framing":
        target = (stat_hint or "the statistic named in the user question").strip()
        extra = QUERY_FRAMING_INSTRUCTIONS.format(stat_name=target)
    else:
        extra = GENERAL_INSTRUCTIONS
    return (
        f"{extra}\n\n"
        f"CONTEXT:\n{context}\n\n"
        f"USER QUESTION:\n{question}\n"
    )

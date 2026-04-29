from google.adk.agents import LlmAgent


revision_agent = LlmAgent(
    name="revision_agent",
    model="gemini-3-flash-preview",
    instruction="""
    You manage spaced repetition.

    Rules:
    - Review after 1 day
    - Then 3 days
    - Then 7 days

    Insert revision sessions into the plan.

    Return ONLY valid JSON (no other text). Same format as the input plan:
    {"2026-04-15": {"study": [...], "revision": [...]}, ...}
    """,
    output_key="revision_output"
)
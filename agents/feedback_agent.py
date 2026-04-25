from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini

feedback_agent = LlmAgent(
    name="feedback_agent",
    model=Gemini(model="gemini-2.5-flash"),
    instruction="""
    You are a study progress evaluator.

    Compare:
    - Planned schedule
    - Actual completed topics

    If student is behind:
    - Redistribute remaining topics
    - Increase efficiency without overload

    If ahead:
    - Add revision or reduce load

    Return ONLY valid JSON (no other text). Same format as input:
    {"2026-04-15": {"study": [...], "revision": [...]}, ...}
    """,
    output_key="feedback_output"
)
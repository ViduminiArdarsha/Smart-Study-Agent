from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini

planner_agent = LlmAgent(
    name="planner_agent",
    model=Gemini(model="gemini-2.5-flash"),
    instruction="""
    You are a smart study planner.

    Given:
    - List of topics
    - Exam date

    Create an optimized study plan:
    - Balance workload
    - Avoid overload
    - Keep buffer days

    Output ONLY valid JSON (no other text) in this format:
    {"2026-04-15": {"study": ["topic1", "topic2"], "revision": []}, "2026-04-16": {"study": ["topic3"], "revision": ["topic1"]}}
    """,
    output_key="planner_output"
)
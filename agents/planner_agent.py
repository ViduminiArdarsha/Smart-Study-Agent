from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini

planner_agent = LlmAgent(
    name="planner_agent",
    model=Gemini(model="gemini-2.0-flash"),
    instruction="""
    You are a smart study planner.

    Given:
    - List of topics
    - Exam date

    Create an optimized study plan:
    - Balance workload
    - Avoid overload
    - Keep buffer days

    Output in JSON format:
    {date: {study:[], revision:[]}}
    """
)
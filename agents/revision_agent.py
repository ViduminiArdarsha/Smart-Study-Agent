from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini

revision_agent = LlmAgent(
    name="revision_agent",
    model=Gemini(model="gemini-2.0-flash"),
    instruction="""
    You manage spaced repetition.

    Rules:
    - Review after 1 day
    - Then 3 days
    - Then 7 days

    Insert revision sessions into the plan.

    Return updated plan.
    """
)
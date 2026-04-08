from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini

feedback_agent = LlmAgent(
    name="feedback_agent",
    model=Gemini(model="gemini-2.0-flash"),
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

    Return UPDATED plan in JSON.
    """
)
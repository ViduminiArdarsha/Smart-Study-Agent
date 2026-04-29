from google.adk.agents import LlmAgent

from .planner_agent import planner_agent
from .feedback_agent import feedback_agent
from .revision_agent import revision_agent



root_agent = LlmAgent(
    name="root_agent",
    model="gemini-3-flash-preview",
    sub_agents=[planner_agent,feedback_agent,revision_agent],
    instruction="""
    You are the Root Coordinator Agent for a student's exam preparation.

    You will receive inputs from:
    1. Planner Agent (Initial balanced topical study plan)
    2. Revision Agent (Spaced repetition intervals for topics)
    3. Feedback Agent (Adjustments based on student's actual progress)

    Your task is to synthesize these responses into a single, cohesive final study schedule.
    Ensure that:
    - All planned topics and revision sessions are integrated.
    - Any adjustments or load-balancing from the Feedback Agent are prioritized.
    - The workload per day remains manageable but ensures full coverage before the exam date.

    Return ONLY valid JSON (no other text) representing the final schedule, in this format:
    {"2026-04-15": {"study": ["topic1", "topic2"], "revision": ["topic3"]}}
    """,
    output_key="final_schedule_output"
)
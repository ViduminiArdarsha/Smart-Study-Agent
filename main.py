# import asyncio
# from dotenv import load_dotenv

# from google.adk.runners import Runner
# from google.adk.sessions import InMemorySessionService
# from google.adk.memory import InMemoryMemoryService
# from google.genai import types

# from agents.planner_agent import planner_agent
# from agents.feedback_agent import feedback_agent
# from agents.revision_agent import revision_agent

# from tools.syllabus_parser import parse_syllabus
# from tools.scheduler import create_study_plan

# load_dotenv()

# APP_NAME = "smart_study_agent"
# USER_ID = "student_1"

# session_service = InMemorySessionService()
# memory_service = InMemoryMemoryService()

# #Run Agent Function
# def run_agent(runner, session, prompt):
#     response = runner.run(
#         session_id=session.id,
#         user_id=USER_ID,
#         new_message=types.Content(
#             role="user",
#             parts=[types.Part(text=prompt)]
#         )
#     )

#     final_text = ""

#     for event in response:
#         if hasattr(event, "output_text") and event.output_text:
#             final_text += event.output_text
#         elif hasattr(event, "text") and event.text:
#             final_text += event.text
#     return final_text.strip()


# # Notification Function
# def send_daily_plan(plan, date):
#     try:
#         import json
#         plan = json.loads(plan)
#     except:
#         print("Plan is not valid JSON")
#         print(plan)
#         return

#     if date in plan:
#         print(f"\n Plan for {date}")
#         print("Study:", plan[date]["study"])
#         print("Revision:", plan[date]["revision"])


# #  MAIN FUNCTION
# async def main():

#     # Create session (async)
#     session = await session_service.create_session(
#         app_name=APP_NAME,
#         user_id=USER_ID
#     )

#     planner_runner = Runner(
#     app_name=APP_NAME,
#     agent=planner_agent,
#     session_service=session_service,
#     memory_service=memory_service
#     )

#     revision_runner = Runner(
#         app_name=APP_NAME,
#         agent=revision_agent,
#         session_service=session_service,
#         memory_service=memory_service
#     )

#     feedback_runner = Runner(
#         app_name=APP_NAME,
#         agent=feedback_agent,
#         session_service=session_service,
#         memory_service=memory_service
#     )
#     # Step 1: Input
#     syllabus_text = "Algebra, Calculus, Probability, Statistics"
#     exam_date = "2026-05-10"

#     # Step 2: Parse
#     topics = parse_syllabus(syllabus_text)

#     # Step 3: Initial Plan
#     plan = create_study_plan(topics, exam_date)

#     # Step 4: Planner Agent
#     plan = run_agent(
#     planner_runner,
#     session,
#     f"Topics: {topics}, Exam: {exam_date}"
# )
    

#     # Step 5: Revision Agent
#     plan = run_agent(
#         revision_runner,
#         session,
#         plan
#     )

#     progress = {
#     "completed": ["Algebra"]
#     }
#     # Step 6: Feedback Agent
#     updated_plan = run_agent(
#         feedback_runner,
#         session,
#         f"Plan: {plan}, Progress: {progress}"
#     )


#     # Step 8: Notify
#     send_daily_plan(updated_plan, "2026-04-08")


# # Run program
# if __name__ == "__main__":
#     asyncio.run(main())

#!/usr/bin/env python3
"""
Smart Study Planner Pipeline
Orchestrates study plan creation through Planner → Revision → Feedback agents
"""

import os
import sys
import asyncio
import logging
import json
import re
from typing import Optional, Dict, Any
from dotenv import load_dotenv

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agents.planner_agent import planner_agent
from agents.feedback_agent import feedback_agent
from agents.revision_agent import revision_agent

from tools.syllabus_parser import parse_syllabus
from tools.scheduler import create_study_plan

load_dotenv()

# ===== Part 2: Configuration =====
APP_NAME = "smart_study_planner"
USER_ID = "student_1"
SESSION_ID = "study-session-1"
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

logging.basicConfig(level=logging.getLevelName(os.getenv("LOG_LEVEL", "ERROR")))
log = logging.getLogger(__name__)

session_service = InMemorySessionService()


# ===== Part 3: Define Sequential Agent Pipeline =====
# Note: Using agents from agents/ module, but updating their output tracking
study_pipeline = SequentialAgent(
    name="StudyPlannerPipeline",
    sub_agents=[
        planner_agent,      # Generates initial plan from topics
        revision_agent,     # Adds spaced repetition sessions
        feedback_agent      # Adapts plan based on progress
    ]
)


# ===== Part 4: Setup Runner =====
runner = Runner(app_name=APP_NAME, agent=study_pipeline, session_service=session_service)


# ===== Part 5: Helper Functions =====

def extract_json(text: str) -> Optional[Dict[str, Any]]:
    """Extract JSON from text, handling markdown blocks and extra content."""
    if not text:
        return None
    
    # Try strict JSON parse first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    
    # Try to extract JSON from markdown code blocks
    for pattern in [r'```json\s*(\{.*?\})\s*```', r'```\s*(\{.*?\})\s*```']:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                continue
    
    # Try to find JSON object in text
    match = re.search(r'(\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\})', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    
    return None


def display_plan(plan_data: Dict[str, Any], date: str) -> None:
    """Display the study plan for a specific date."""
    if not plan_data or date not in plan_data:
        available = list(plan_data.keys()) if plan_data else []
        print(f"\n⚠️  No plan found for {date}")
        if available:
            print(f"   Available dates: {available[:3]}...")  # Show first 3
        return
    
    day_plan = plan_data[date]
    print(f"\n📅 Study Plan for {date}")
    print(f"   📚 Study: {day_plan.get('study', [])}")
    print(f"   🔄 Revision: {day_plan.get('revision', [])}")


def print_pipeline_summary(state: Dict[str, Any]) -> None:
    """Print pipeline execution summary."""
    print("\n" + "=" * 50)
    print("📊 Pipeline Execution Summary")
    print("=" * 50)
    
    stages = [
        ("planner_output", "1️⃣  Plan Generation"),
        ("revision_output", "2️⃣  Revision Scheduling"),
        ("feedback_output", "3️⃣  Feedback Adaptation")
    ]
    
    for key, label in stages:
        status = "✅ Complete" if key in state and state[key] else "⏭️  Skipped"
        print(f"{label}: {status}")


async def run_study_pipeline(
    syllabus_text: str,
    exam_date: str,
    progress: Optional[Dict[str, Any]] = None,
    review_date: str = "2026-04-11"
) -> Dict[str, Any]:
    """
    Execute the study planning pipeline.
    
    Args:
        syllabus_text: Topics to study (comma-separated)
        exam_date: Exam date (YYYY-MM-DD)
        progress: Student progress (optional)
        review_date: Date to display plan for
    
    Returns:
        Dictionary with pipeline results and state
    """
    # Create session
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state={}
    )
    
    # Parse topics and create initial plan
    topics = parse_syllabus(syllabus_text)
    initial_plan = create_study_plan(topics, exam_date)
    
    # Build pipeline prompt
    progress_text = json.dumps(progress) if progress else "{}"
    pipeline_prompt = (
        f"Create a study plan for these topics: {topics}\n"
        f"Exam date: {exam_date}\n"
        f"Initial schedule: {initial_plan}\n"
        f"Student progress: {progress_text}\n\n"
        f"Generate the complete plan in JSON format."
    )
    
    print("\n🚀 Starting Study Planner Pipeline...")
    print(f"   Syllabus: {syllabus_text}")
    print(f"   Exam Date: {exam_date}\n")
    
    # Run pipeline with async iteration
    message = types.Content(role='user', parts=[types.Part(text=pipeline_prompt)])
    response_text = ""
    
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=message
    ):
        if event.is_final_response() and event.content and event.content.parts:
            response_text = event.content.parts[0].text
    
    # Retrieve session state
    session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    
    state = session.state if session else {}
    
    return {
        "response": response_text,
        "state": state,
        "review_date": review_date
    }


async def main() -> None:
    """Main entry point orchestrating the pipeline."""
    print("\n" + "=" * 50)
    print("🎓 Smart Study Planner Pipeline")
    print("=" * 50)
    
    try:
        # Input parameters
        syllabus_text = "Algebra, Calculus, Probability, Statistics"
        exam_date = "2026-05-10"
        progress = {"completed": ["Algebra"], "in_progress": ["Calculus"]}
        review_date = "2026-04-08"
        
        # Run pipeline
        result = await run_study_pipeline(
            syllabus_text=syllabus_text,
            exam_date=exam_date,
            progress=progress,
            review_date=review_date
        )
        
        # Display results
        print_pipeline_summary(result.get("state", {}))
        
        # Extract and display final plan
        final_plan = extract_json(result.get("response", ""))
        if final_plan:
            display_plan(final_plan, result["review_date"])
        else:
            print("\n❌ Failed to parse final plan")
            if result.get("response"):
                print(f"Raw response: {result['response'][:200]}...")
    
    except Exception as e:
        log.error(f"Pipeline failed: {e}", exc_info=True)
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    # Set event loop policy for Windows compatibility
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    # Run pipeline
    asyncio.run(main())
import asyncio
from dotenv import load_dotenv

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.memory import InMemoryMemoryService
from google.genai import types

from agents.planner_agent import planner_agent
from agents.feedback_agent import feedback_agent
from agents.revision_agent import revision_agent

from tools.syllabus_parser import parse_syllabus
from tools.scheduler import create_study_plan

load_dotenv()

APP_NAME = "smart_study_agent"
USER_ID = "student_1"

session_service = InMemorySessionService()
memory_service = InMemoryMemoryService()

#Run Agent Function
def run_agent(runner, session, prompt):
    response = runner.run(
        session_id=session.id,
        user_id=USER_ID,
        new_message=types.Content(
            role="user",
            parts=[types.Part(text=prompt)]
        )
    )

    if hasattr(response, "output_text"):
        return response.output_text
    elif hasattr(response, "text"):
        return response.text
    else:
        return str(response)


# Notification Function
def send_daily_plan(plan, date):
    try:
        import json
        plan = json.loads(plan)
    except:
        print("Plan is not valid JSON")
        print(plan)
        return

    if date in plan:
        print(f"\n Plan for {date}")
        print("Study:", plan[date]["study"])
        print("Revision:", plan[date]["revision"])


#  MAIN FUNCTION
async def main():

    # Create session (async)
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID
    )

    planner_runner = Runner(
    app_name=APP_NAME,
    agent=planner_agent,
    session_service=session_service,
    memory_service=memory_service
    )

    revision_runner = Runner(
        app_name=APP_NAME,
        agent=revision_agent,
        session_service=session_service,
        memory_service=memory_service
    )

    feedback_runner = Runner(
        app_name=APP_NAME,
        agent=feedback_agent,
        session_service=session_service,
        memory_service=memory_service
    )
    # Step 1: Input
    syllabus_text = "Algebra, Calculus, Probability, Statistics"
    exam_date = "2026-05-10"

    # Step 2: Parse
    topics = parse_syllabus(syllabus_text)

    # Step 3: Initial Plan
    plan = create_study_plan(topics, exam_date)

    # Step 4: Planner Agent
    plan = run_agent(
    planner_runner,
    session,
    f"Topics: {topics}, Exam: {exam_date}"
)
    

    # Step 5: Revision Agent
    plan = run_agent(
        revision_runner,
        session,
        plan
    )

    progress = {
    "completed": ["Algebra"]
    }
    # Step 6: Feedback Agent
    updated_plan = run_agent(
        feedback_runner,
        session,
        f"Plan: {plan}, Progress: {progress}"
    )


    # Step 8: Notify
    send_daily_plan(updated_plan, "2026-04-08")


# Run program
if __name__ == "__main__":
    asyncio.run(main())
from dotenv import load_dotenv
import os

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.memory import InMemoryMemoryService

load_dotenv()

APP_NAME = "smart_study_agent"
USER_ID = "student_1"

session_service = InMemorySessionService()
memory_service = InMemoryMemoryService()

runner = Runner(
    app_name=APP_NAME,
    session_service=session_service,
    memory_service=memory_service
)
import logging
import os

import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import(
    AgentCapabilities,
    AgentCard,
    AgentSkill
)

from agent import create_agent
from agent_executer import ApekshaAgentExecuter

from dotenv import load_dotenv
from google.adk.artifacts import InMemoryArtifactService
from google.adk.memory.in_memory_memory_service import InMemoryMemoryService
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

load_dotenv()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    host = "localhost"
    port = 10002

    try:
        capabilities = AgentCapabilities(streaming=True)

        skill = AgentSkill(
            id="check_schedule",
            name="Check Apeksha's schedule",
            description="Checks Apeksha's availability for a pickleball game on a given date.",
            tags=["scheduling", "calendar"],
            examples=["Is Apeksha free to play pickleball tomorrow?"],
        )

        agent_card = AgentCard(
            name="Apeksha Agent",
            description="An agent that manages Apeksha's schedule for pickleball games.",
            url=f"http://{host}:{port}/",
            version="1.0.0",
            defaultInputModes=["text/plain"],
            defaultOutputModes=["text/plain"],
            capabilities=capabilities,
            skills=[skill],
        )

        adk_agent = create_agent()

        runner = Runner(
            app_name=agent_card.name,
            agent=adk_agent,
            artifact_service=InMemoryArtifactService(),
            session_service=InMemorySessionService,
            memory_service=InMemoryMemoryService()
        )

        agent_executor = ApekshaAgentExecuter(runner)

        request_handler = DefaultRequestHandler(
            agent_executor=agent_executor,
            task_store=InMemoryTaskStore()
        )

        server = A2AStarletteApplication(
            agent_card=agent_card,
            http_handler=request_handler
        )
        uvicorn.run(server.build, host=host, port=port)
    except Exception as e:
        logger.error(f"An error occurred during server startup: {e}")
        exit(1)


if __name__ == "__main__":
    main()
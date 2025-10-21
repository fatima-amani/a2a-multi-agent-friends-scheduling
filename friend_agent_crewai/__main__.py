import logging
import os

import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)
from agent import SchedulingAgent
from agent_executor import SchedulingAgentExecutor
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    host="localhost"
    port=10003

    try:
        capabilities = AgentCapabilities(streaming=False)

        skill = AgentSkill(
             id="availability_checker",
            name="Availability Checker",
            description="Check my calendar to see when I'm available for a pickleball game.",
            tags=["schedule", "availability", "calendar"],
            examples=[
                "Are you free tomorrow?",
                "Can you play pickleball next Tuesday at 5pm?",
            ],
        )

        agent_host_url = f"http://{host}:{port}"

        agent_card = AgentCard(
            name="Alaka Agent",
             description="A friendly agent to help you schedule a pickleball game with Alaka.",
            url=agent_host_url,
            version="1.0.0",
            default_input_modes=SchedulingAgent.SUPPORTED_CONTENT_TYPES,
            default_output_modes=SchedulingAgent.SUPPORTED_CONTENT_TYPES,
            capabilities=capabilities,
            skills=[skill]
        )

        request_handler = DefaultRequestHandler(
            agent_executor=SchedulingAgentExecutor(),
            task_store=InMemoryTaskStore()
        )

        server = A2AStarletteApplication(
            agent_card=agent_card,
            http_handler=request_handler
        )

        uvicorn.run(server.build(), host=host, port=port)
    except Exception as e:
        logger.error(f"An error occurred during server startup: {e}")
        exit(1)


if __name__ == "__main__":
    main()
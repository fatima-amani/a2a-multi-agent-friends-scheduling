import logging
import os
import sys

import httpx
import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import PushNotificationSender, InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)
from app.agent import AamnaAgent
from app.agent_executor import AamnaAgentExecutor
from dotenv import load_dotenv
from starlette.responses import JSONResponse

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Starts Aamna's Agent server."""
    host = "localhost"
    port = 10004
    try:
        capabilities = AgentCapabilities(streaming=True, pushNotifications=True)
        skill = AgentSkill(
            id="schedule_pickleball",
            name="Pickleball Scheduling Tool",
            description="Helps with finding Aamna's availability for pickleball",
            tags=["scheduling", "pickleball"],
            examples=["Are you free to play pickleball on Saturday?"],
        )
        agent_card = AgentCard(
            name="Aamna Agent",
            description="Helps with scheduling pickleball games",
            url=f"http://{host}:{port}/",
            version="1.0.0",
            defaultInputModes=AamnaAgent.SUPPORTED_CONTENT_TYPES,
            defaultOutputModes=AamnaAgent.SUPPORTED_CONTENT_TYPES,
            capabilities=capabilities,
            skills=[skill],
        )

        httpx_client = httpx.AsyncClient()
        request_handler = DefaultRequestHandler(
            agent_executor=AamnaAgentExecutor(),
            task_store=InMemoryTaskStore(),
        )
        server = A2AStarletteApplication(
            agent_card=agent_card, http_handler=request_handler
        )

        app = server.build()

        app = server.build()
        
        @app.route('/.well-known/agent-card.json')
        async def well_known_agent_card(request):
            return JSONResponse(agent_card.dict())
        
        uvicorn.run(app, host=host, port=port)

    except Exception as e:
        logger.error(f"An error occurred during server startup: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
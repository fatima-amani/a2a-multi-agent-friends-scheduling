import asyncio
import logging
from collections.abc import AsyncGenerator

from a2a.server.agent_execution import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.server.tasks import TaskUpdater
from a2a.types import (
    FilePart,
    FileWithBytes, FileWithUri, Part, TaskState, InvalidParamsError,
    TextPart, UnsupportedOperationError, InternalError
)
from a2a.utils.errors import ServerError

from agent import create_agent
from agents import Agent, Runner, function_tool


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class DarshanaAgentExecutor(AgentExecutor):

    def __init__(self):
        self.agent = create_agent()
    
    async def execute(self, context: RequestContext, event_queue: EventQueue):
        if not context.task_id or not context.context_id:
            raise ValueError("RequestContext must have task_id and context_id")
        if not context.message:
            raise ValueError("RequestContext must have a message")

        updater = TaskUpdater(event_queue, context.task_id, context.context_id)
        if not context.current_task:
            await updater.submit()
        await updater.start_work()

        if self._validate_request(context):
            raise ServerError(error=InvalidParamsError())
        
        query = context.get_user_input()

        try:
            result = await Runner.run(self.agent, input=query)
            print(f"Final Result: {result}")
        except Exception as e:
            print(f"Error invoking agent: {e}")
            raise ServerError(error=InternalError()) from e
        parts = [Part(root=TextPart(text=result.final_output))]

        await updater.add_artifact(parts)
        await updater.complete()
    
    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        """Handles task cancellation."""
        raise ServerError(error=UnsupportedOperationError())

    def _validate_request(self, context: RequestContext) -> bool:
        """Validates the request context."""
        return False
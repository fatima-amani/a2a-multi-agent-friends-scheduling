# Friend Agent (LangGraph)

This agent is part of the Friend Scheduling project. It is built using LangGraph.

## Libraries Used

-   `a2a-sdk`
-   `httpx`
-   `langchain-google-genai`
-   `langgraph`
-   `pydantic`
-   `python-dotenv`
-   `uvicorn`
-   `langchain-core`

## Available Tools

-   `get_availability(date_range: str)`: Use this to get Kaitlyn's availability for a given date or date range.

## Agent Card

This agent is a LangGraph agent. It exposes a custom endpoint that the host agent can use to interact with it.

## Running the Agent

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/fatima-amani/a2a-multi-agent-friends-scheduling.git
    cd friend_scheduling/friend_agent_langgraph
    ```

2.  **Initialize the environment:**
    ```bash
    uv init
    ```

3.  **Sync dependencies:**
    ```bash
    uv sync
    ```

4.  **Run the agent:**
    ```bash
    uv run python -m app
    ```

5.  **Access the Agent Card:**
    Open your browser and go to `http://localhost:10004/.well-known/agent-card.json` to see the agent card.
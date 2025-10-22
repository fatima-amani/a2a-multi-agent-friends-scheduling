# Friend Agent (Google ADK)

This agent is part of the Friend Scheduling project. It is built using the Agent Development Kit (ADK).

## Libraries Used

-   `a2a-sdk`
-   `google-adk`
-   `python-dotenv`
-   `uvicorn`

## Available Tools

-   `get_availability(start_date: str, end_date: str)`: Checks the agent's availability for a given date range.

## Agent Card

This agent is an ADK agent. Its endpoint is managed by the ADK runtime and can be discovered by the host agent.

## Running the Agent

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/fatima-amani/a2a-multi-agent-friends-scheduling.git
    cd friend_scheduling/friend_agent_adk
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
    uv run .
    ```

5.  **Access the Agent Card:**
    Open your browser and go to `http://localhost:10002/.well-known/agent-card.json` to see the agent card.
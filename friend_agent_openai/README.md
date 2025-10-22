# Friend Agent (OpenAI)

This agent is part of the Friend Scheduling project. It is built using the OpenAI Assistants API.

## Libraries Used

-   `a2a-sdk`
-   `openai-agents`

## Available Tools

-   `get_availability(start_date: str, end_date: str)`: Checks the agent's availability for a given date range.

## Agent Card

This agent is an OpenAI agent. It exposes a custom endpoint that the host agent can use to interact with it.

## Running the Agent

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/fatima-amani/a2a-multi-agent-friends-scheduling.git
    cd friend_scheduling/friend_agent_openai
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
    Open your browser and go to `http://localhost:10005/.well-known/agent-card.json` to see the agent card.

# Friend Scheduling Agent - CrewAI

This agent is part of the Friend Scheduling project. It is built using CrewAI.

## Libraries Used

-   `a2a-sdk`
-   `crewai[google-genai,tools]`
-   `google-generativeai`
-   `pydantic`
-   `python-dotenv`
-   `uvicorn`

## Available Tools

-   `AvailabilityTool(date_range: str)`: Checks the agent's availability for a given date or date range.

## Agent Card

This agent is a CrewAI agent. It exposes a custom endpoint that the host agent can use to interact with it.

## Running the Agent

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/fatima-amani/a2a-multi-agent-friends-scheduling.git
    cd friend_scheduling/friend_agent_crewai
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
    uv run
    ```

5.  **Access the Agent Card:**
    Open your browser and go to `http://localhost:10003/.well-known/agent-card.json` to see the agent card.
# Host Agent

This agent is the central coordinator for the Friend Scheduling project. It is built using the Google Agent Development Kit (ADK).

## Libraries Used

-   `a2a`
-   `a2a-sdk`
-   `click`
-   `google-adk`
-   `google-generativeai`
-   `httpx`
-   `nest-asyncio`
-   `python-dotenv`
-   `uvicorn`

## Available Tools

-   `send_message(agent_name: str, task: str)`: Sends a message to a remote friend agent to ask for their availability.
-   `list_court_availabilities(date: str)`: Lists the available and booked time slots for the pickleball court on a given date.
-   `book_pickleball_court(date: str, start_time: str, end_time: str, reservation_name: str)`: Books the pickleball court for a given date and time.

## Agent Card

This is the host agent and it runs as an ADK web application. It connects to the remote friend agents to coordinate scheduling.

## Running the Agent

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/fatima-amani/a2a-multi-agent-friends-scheduling.git
    cd friend_scheduling/host_agent
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
    uv run adk web
    ```

5.  **Access the Host Agent UI:**
    Open your browser and go to `http://localhost:8000` to interact with the host agent.
# A2A PickleBall Scheduling Multi-Agent System

This project implements a multi-agent system using A2A Protocol for scheduling activities among friends. It uses a2a to communicate between different agents made using Google ADK, OpenAI agents, CrewAI, and LangGraph. The project consists of a host client agent and four friend agents, each simulating one of the developer's friends.

-   **Host Agent**: The central coordinator.
-   **Friend Agent (ADK)**: A friend agent built with the Agent Development Kit.
-   **Friend Agent (CrewAI)**: A friend agent built with CrewAI.
-   **Friend Agent (LangGraph)**: A friend agent built with LangGraph.
-   **Friend Agent (OpenAI)**: A friend agent built with the OpenAI Agents.

## Repository

The source code is available on GitHub: [https://github.com/fatima-amani/a2a-multi-agent-friends-scheduling](https://github.com/fatima-amani/a2a-multi-agent-friends-scheduling)

## Running the Agents

To run the agents, you will need to have `uv` installed.

### 1. Clone the Repository

```bash
git clone https://github.com/fatima-amani/a2a-multi-agent-friends-scheduling.git
cd a2a-multi-agent-friends-scheduling
```

### 2. Run the Host Agent

In a new terminal window:

```bash
cd host_agent
uv init
uv sync
uv run adk web
```

Open your browser and go to `http://localhost:8000` to interact with the host agent.

### 3. Run the Friend Agent (ADK)

In a new terminal window:

```bash
cd friend_agent_adk
uv init
uv sync
uv run .
```

### 4. Run the Friend Agent (CrewAI)

In a new terminal window:

```bash
cd friend_agent_crewai
uv init
uv sync
uv run .
```

### 5. Run the Friend Agent (LangGraph)

In a new terminal window:

```bash
cd friend_agent_langgraph
uv init
uv sync
uv run .
```

### 6. Run the Friend Agent (OpenAI)

In a new terminal window:

```bash
cd friend_agent_openai
uv init
uv sync
uv run .
```

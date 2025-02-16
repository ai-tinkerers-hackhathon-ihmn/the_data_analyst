"""`backend.agents.orchestrator` module.

Orchestrator agent.
Responsible for coordinating the other agents.

"""

from smolagents import CodeAgent, LiteLLMModel

from backend.agents.query_analyzer import query_analyzer
from backend.agents.report_generator import report_generator

MODEL_ID: str = "anthropic/claude-3-5-sonnet-latest"

llm = LiteLLMModel(
    model_id=MODEL_ID,
)

orchestrator = CodeAgent(
    name="orchestrator",
    description="Orchestrates the other agents.",
    model=llm,
    managed_agents = [
        query_analyzer,
        report_generator,
    ],
    tools = [],
    add_base_tools = True,
    max_steps = 12
)

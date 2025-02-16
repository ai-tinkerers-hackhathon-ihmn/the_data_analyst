"""`backend.agents.orchestrator` module.

Orchestrator agent.
Responsible for coordinating the other agents.

"""

from smolagents import CodeAgent

from backend.agents.query_analyzer import query_analyzer
from backend.agents.report_generator import report_generator

orchestrator = CodeAgent(
    name="orchestrator",
    description="Orchestrates the other agents.",
    managed_agents = [
        query_analyzer,
        report_generator,
    ],
)

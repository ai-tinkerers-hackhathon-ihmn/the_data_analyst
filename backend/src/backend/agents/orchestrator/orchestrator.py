"""`backend.agents.orchestrator` module.

Orchestrator agent.
Responsible for coordinating the other agents.

"""

from smolagents import CodeAgent, LiteLLMModel

from backend.agents.query_analyzer.query_analyzer import query_analyzer
from backend.agents.report_generator.report_generator import report_generator
from backend.agents.orchestrator.system_prompt import SYSTEM_PROMPT

MODEL_ID: str = "anthropic/claude-3-5-sonnet-latest"


def build_orchestrator() -> CodeAgent:
    """Builds the orchestrator agent."""
    
    llm = LiteLLMModel(
        model_id=MODEL_ID,
    )

    orchestrator = CodeAgent(
        name="orchestrator",
        description="Orchestrates the other agents.",
        model=llm,
        managed_agents=[
            query_analyzer,
            report_generator,
        ],
        tools=[],
        add_base_tools=True,
        max_steps=12
    )
    
    # Override the system prompt
    orchestrator.prompt_templates["system_prompt"] = SYSTEM_PROMPT

    return orchestrator


orchestrator = build_orchestrator()

"""`backend.agents.report_generator` module."""

from smolagents import CodeAgent, LiteLLMModel
from backend.tools.python_tools import AUTHORIZED_IMPORTS

MODEL_ID: str = "anthropic/claude-3-5-sonnet-latest"

llm = LiteLLMModel(
    model_id=MODEL_ID,
)


report_generator = CodeAgent(
    model=llm,
    name="report_generator",
    description="Generates business reports from insights provided by another agent.",
    tools=[],
    additional_authorized_imports = AUTHORIZED_IMPORTS,
    # add_base_tools = True,
    max_steps =12
)
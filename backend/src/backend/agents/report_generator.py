"""`backend.agents.report_generator` module."""

from smolagents import CodeAgent, LiteLLMModel

MODEL_ID: str = "anthropic/claude-3-5-sonnet-latest"

llm = LiteLLMModel(
    model_id=MODEL_ID,
)


report_generator = CodeAgent(
    model=llm,
    name="report_generator",
    description="Generates business reports from insights provided by another agent.",
    tools = [],
    add_base_tools = True
)
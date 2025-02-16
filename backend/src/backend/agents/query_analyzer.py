"""`backend.agents.query_analyzer` module."""

from smolagents import CodeAgent, LiteLLMModel


MODEL_ID: str = "anthropic/claude-3-5-sonnet-latest"

llm = LiteLLMModel(
    model_id=MODEL_ID,
)


query_analyzer = CodeAgent(
    model=llm,
    name="query_analyzer",
    description="Analyzes user queries and retrieves the necessary data from the database.",
    tools = [],
    add_base_tools = True,
    max_steps = 12
)
"""`backend.agents.query_analyzer` module."""

import os
from smolagents import CodeAgent, LiteLLMModel


from backend.tools.postgre_tool import PostgresQueryTool


MODEL_ID: str = "anthropic/claude-3-5-sonnet-latest"

llm = LiteLLMModel(
    model_id=MODEL_ID,
    temperature=0.6,
    api_key=os.environ["ANTHROPIC_API_KEY"]
)


query_analyzer = CodeAgent(
    name="query_analyzer",
    description="Analyzes user queries and retrieves the necessary data from the database.",
    max_steps = 12,
    tools = [PostgresQueryTool()],
    model=llm,
    add_base_tools = True,
)


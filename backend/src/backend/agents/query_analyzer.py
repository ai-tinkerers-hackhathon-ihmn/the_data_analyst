"""`backend.agents.query_analyzer` module."""

from smolagents import CodeAgent, LiteLLMModel

## import relevant tools
import sys
sys.path.append('../')
from tools.postgre_tool import PostgresQueryTool


MODEL_ID: str = "anthropic/claude-3-5-sonnet-latest"

llm = LiteLLMModel(
    model_id=MODEL_ID,
)


query_analyzer = CodeAgent(
    model=llm,
    name="query_analyzer",
    description="Analyzes user queries and retrieves the necessary data from the database.",
    tools = [PostgresQueryTool()],
    model = model,
  add_base_tools = True
)


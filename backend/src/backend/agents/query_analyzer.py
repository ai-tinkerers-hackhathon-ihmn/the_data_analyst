"""`backend.agents.query_analyzer` module."""
import os 
from smolagents import CodeAgent, LiteLLMModel, ToolCallingAgent

from backend.tools.postgre_tool import PostgresQueryTool
from backend.tools.mongodb_tool import MongoDBQueryTool

MODEL_ID: str = "anthropic/claude-3-5-sonnet-latest"

llm = LiteLLMModel(
    model_id=MODEL_ID,
    temperature=0,
    api_key=os.environ["ANTHROPIC_API_KEY"]
)

query_analyzer = CodeAgent(
    name="query_analyzer",
    description="Analyzes user queries and retrieves the necessary data from the database.",
    model=llm,
    max_steps=12,
    tools = [PostgresQueryTool(), MongoDBQueryTool()],
    # add_base_tools = True,
    verbosity_level=3,
)


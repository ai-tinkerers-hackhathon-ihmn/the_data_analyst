"""`backend.agents.query_analyzer` module."""

from smolagents import CodeAgent, LiteLLMModel

## import relevant tools
import sys
import os

import dotenv

dotenv.load_dotenv()

sys.path.append('../')
from tools.postgre_tool import PostgresQueryTool
from tools.mongodb_tool import MongoDBQueryTool


MODEL_ID: str = "anthropic/claude-3-5-sonnet-latest"

llm = LiteLLMModel(
    model_id=MODEL_ID,
    temperature=0.6,
    api_key=os.environ["ANTHROPIC_API_KEY"]
)


query_analyzer = CodeAgent(
    name="query_analyzer",
    description="Analyzes user queries and retrieves the necessary data from the database.",
    tools = [PostgresQueryTool(), MongoDBQueryTool()],
    model=llm,
    add_base_tools = True,
)


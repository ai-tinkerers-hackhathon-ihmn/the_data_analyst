"""`backend.agents.query_analyzer` module."""

from smolagents import CodeAgent, LiteLLMModel

## import relevant tools
import sys
sys.path.append('../')
from tools.postgre_tool import PostgresQueryTool

model = LiteLLMModel(model_id="anthropic/claude-3-5-sonnet-latest", 
                     api_key="YOUR_ANTHROPIC_API_KEY") 

query_analyzer = CodeAgent(
    name="query_analyzer",
    description="Analyzes user queries and retrieves the necessary data from the database.",
    tools = [PostgresQueryTool()],
    model = model
)

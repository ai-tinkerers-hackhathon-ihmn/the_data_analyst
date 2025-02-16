"""`backend.agents.query_analyzer` module."""

from smolagents import CodeAgent

query_analyzer = CodeAgent(
    name="query_analyzer",
    description="Analyzes user queries and retrieves the necessary data from the database.",
)
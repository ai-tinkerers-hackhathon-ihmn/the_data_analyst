"""`backend.agents.report_generator` module."""

from smolagents import CodeAgent

report_generator = CodeAgent(
    name="report_generator",
    description="Generates business reports from insights provided by another agent.",
)
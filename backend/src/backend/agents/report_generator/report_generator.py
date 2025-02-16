"""`backend.agents.report_generator` module."""

from smolagents import CodeAgent, LiteLLMModel
from backend.tools.python_tools import AUTHORIZED_IMPORTS
from backend.agents.report_generator.system_prompt import SYSTEM_PROMPT
from backend.tools.streamlit_dashboard_generator import setup_default_dashboard, create_dashboard_section

MODEL_ID: str = "anthropic/claude-3-5-sonnet-latest"


def build_report_generator()->CodeAgent:
    """Builds the report generator agent."""

    llm = LiteLLMModel(
    model_id=MODEL_ID,
)

    report_generator = CodeAgent(
        model=llm,
        additional_authorized_imports = AUTHORIZED_IMPORTS,
        name="report_generator",
        description="Generates business reports from insights provided by another agent.",
        tools = [setup_default_dashboard, create_dashboard_section],
        add_base_tools = True,
        max_steps = 12,
    )
    # Override the system prompt
    report_generator.prompt_templates["system_prompt"] = SYSTEM_PROMPT

    return report_generator

report_generator = build_report_generator()

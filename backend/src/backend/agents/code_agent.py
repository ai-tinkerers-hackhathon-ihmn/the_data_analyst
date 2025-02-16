"""`backend.agents.report_generator` module."""

from smolagents import CodeAgent, LiteLLMModel, PythonInterpreterTool
from backend.tools.python_tools import AUTHORIZED_IMPORTS
from tools import google_search, serper_scrape, python_file

MODEL_ID: str = "anthropic/claude-3-5-sonnet-latest"

llm = LiteLLMModel(
    model_id=MODEL_ID,
)


code_agent = CodeAgent(
    model=llm,
    name="code_agent",
    description="Generates Streamlit Python code base on the analysis from the report generator",
    tools = [PythonInterpreterTool(), python_file.file_creator], # create_python_file_and_run_it
    add_base_tools = True,
    additional_authorized_imports = AUTHORIZED_IMPORTS,
    max_steps = 12
)
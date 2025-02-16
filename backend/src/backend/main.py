"""`backend.main` module.

Entry point for the backend.
"""

from smolagents import GradioUI
from backend.agents.orchestrator.orchestrator import orchestrator
from backend.setup import setup
from backend.prompt_injection import modify_user_prompt

def main()->None:
    """Entry point for the backend."""
    print("Hello, world!")

    # setup()
    # print(orchestrator.managed_agents["report_generator"].prompt_templates["system_prompt"])
    # ui = GradioUI(orchestrator)
    # ui.launch()

    from backend.examples import DEMO_TASK
    from backend.agents.report_generator.report_generator import report_generator
    orchestrator.run(DEMO_TASK)




if __name__ == "__main__":
    main()

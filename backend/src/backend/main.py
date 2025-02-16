"""`backend.main` module.

Entry point for the backend.
"""

from smolagents import GradioUI
from backend.agents.orchestrator import orchestrator
from backend.setup import setup

def main()->None:
    """Entry point for the backend."""
    print("Hello, world!")
    setup()
    ui = GradioUI(orchestrator)
    ui.launch()




if __name__ == "__main__":
    main()

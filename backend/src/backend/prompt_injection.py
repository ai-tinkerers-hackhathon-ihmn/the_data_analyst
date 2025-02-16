
from copy import copy

def modify_user_prompt(prompt: str) -> str:
    """Modify the user prompt to include the system prompt."""

    new_prompt = copy(prompt)
    
    new_prompt += "\n\n" 
    new_prompt += """
    Work iteratively to build the report. The end goal is to generate the code to build a streamlit dashboard.
    The dashboard should feature data tables and charts to help the user understand the report.

    """

    return new_prompt

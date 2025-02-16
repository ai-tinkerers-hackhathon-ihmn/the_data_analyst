"""`backend.setup` module."""

from dotenv import load_dotenv

def setup()->None:
    """Setup the backend."""
    load_dotenv()

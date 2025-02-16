"""`backend.tools.google_search` module."""

import os
import json
from typing import Dict, Any

import requests
from smolagents import Tool

class GoogleSearch(Tool):
    name = "google_search"
    description = "Searches Google for a given query."
    inputs = {
        "query": {
            "type": "string",
            "description": "The search query. For example ''"
        },
    }
    output_type = "string"

    def __init__(self):
        super().__init__()
        self.url = "https://google.serper.dev/search"
        self.headers = {
            'X-API-KEY': os.environ["SERPER_API"],
            'Content-Type': 'application/json'
        }

    def forward(self, query: str) -> Dict[str, Any]:
        """Executes the Google search."""
        payload = {
            "q": query,
            "num": 10,
        }

        response = requests.request("POST", self.url, headers=self.headers, data=json.dumps(payload))
        return response.text  
google_search = GoogleSearch()

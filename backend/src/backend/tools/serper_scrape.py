"""`backend.tools.google_search` module."""

import os
import json
from typing import Dict, Any

import requests
from smolagents import Tool


class SerperScrape(Tool):
    name = "serper_scrape"
    description = "Scrapes a website using Serper.dev API to extract information with markdown formatting."
    inputs = {
        "url": {
            "type": "string",
            "description": "The URL or website name to scrape."
        },
    }
    output_type = "string"

    def __init__(self):
        super().__init__()
        self.url = "https://scrape.serper.dev"
        self.headers = {
            'X-API-KEY': os.environ["SERPER_API"],
            'Content-Type': 'application/json'
        }

    def forward(self, url: str) -> str:
        """Executes the Serper.dev website scrape."""
        payload = json.dumps({
            "url": url,
            "includeMarkdown": True
        })

        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response.text
    
serper_scrape = SerperScrape()

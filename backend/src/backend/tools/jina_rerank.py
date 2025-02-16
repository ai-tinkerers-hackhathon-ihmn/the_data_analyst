"""`backend.tools.jina_rerank` module."""

import os
import requests
from smolagents import Tool

class JinaRerank(Tool):
    name = "jina_rerank"
    description = "Reranks documents or links using Jina AI's reranking model."
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to rerank documents or links against."
        },
        "documents": {
            "type": "array",
            "description": "List of documents or links to rerank."
        },
    }
    output_type = "string"

    def __init__(self):
        super().__init__()
        self.url = "https://api.jina.ai/v1/rerank"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {os.environ["JINA_API_KEY"]}'
        }

    def forward(self, query: str, documents: list) -> str:
        """Executes the Jina AI reranking."""
        payload = {
            "model": "jina-reranker-v2-base-multilingual",
            "query": query,
            "top_n": 3,
            "documents": documents
        }

        response = requests.post(self.url, headers=self.headers, json=payload)
        return response.json()
    
jina_rerank = JinaRerank()
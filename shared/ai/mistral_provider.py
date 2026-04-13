import requests
import os
from shared.ai.base_provider import BaseAIProvider
from shared.ai.ai_config import AIConfig

class MistralProvider(BaseAIProvider):
    def __init__(self):
        self.name = "mistral"
        self.api_key = os.getenv("MISTRAL_API_KEY")
        if not self.api_key:
            raise ValueError("MISTRAL_API_KEY environment variable is not set.")
        self.url = "https://api.mistral.ai/v1/chat/completions"

    def generate(self, prompt: str, config: AIConfig = None) -> str:
        if not prompt:
            raise ValueError("Prompt cannot be empty.")
        if config is None:
            config = AIConfig()
        request_data = {
            "model": config.model if config.model else "mistral-small",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": config.temperature if config.temperature is not None else 0.2
        }
        if config.max_tokens is not None:
            request_data["max_tokens"] = config.max_tokens
        if config.top_p is not None:
            request_data["top_p"] = config.top_p
        
        response = requests.post(
            self.url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            json=request_data
        )

        data = response.json()
        return data["choices"][0]["message"]["content"]
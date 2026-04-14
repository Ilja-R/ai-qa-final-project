import requests
import os
from shared.ai.base_provider import BaseAIProvider
from shared.ai.ai_config import AIConfig
from shared.utils.logger import app_logger

class GeminiProvider(BaseAIProvider):
    def __init__(self):
        self.name = "gemini"
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            app_logger.error("GEMINI_API_KEY environment variable is not set.")
            raise ValueError("GEMINI_API_KEY environment variable is not set.")
        # Using the Google Generative AI REST API endpoint
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"

    def generate(self, prompt: str, config: AIConfig = None) -> str:
        if not prompt:
            raise ValueError("Prompt cannot be empty.")
        if config is None:
            config = AIConfig()
        
        model = config.model if config.model else "gemini-1.5-flash"
        url = f"{self.base_url}/{model}:generateContent?key={self.api_key}"
        
        generation_config = {}
        if config.temperature is not None:
            generation_config["temperature"] = config.temperature
        else:
            generation_config["temperature"] = 0.2
            
        if config.max_tokens is not None:
            generation_config["maxOutputTokens"] = config.max_tokens
        if config.top_p is not None:
            generation_config["topP"] = config.top_p

        request_data = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": generation_config
        }
        
        try:
            app_logger.info(f"Sending request to Gemini API with model: {model}")
            response = requests.post(
                url,
                headers={
                    "Content-Type": "application/json"
                },
                json=request_data,
                timeout=30
            )

            if response.status_code != 200:
                app_logger.error(f"Gemini API request failed with status {response.status_code}: {response.text}")
                raise Exception(f"Gemini API request failed with status {response.status_code}: {response.text}")

            data = response.json()
            
            try:
                return data["candidates"][0]["content"]["parts"][0]["text"]
            except (KeyError, IndexError) as e:
                app_logger.error(f"Failed to parse Gemini response: {data}")
                raise Exception(f"Failed to parse Gemini response: {data}") from e
        except requests.exceptions.RequestException as e:
            app_logger.error(f"Gemini API request failed: {str(e)}")
            raise Exception(f"Gemini API request failed: {str(e)}")
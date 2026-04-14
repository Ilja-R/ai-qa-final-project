import requests
import os
from shared.ai.base_provider import BaseAIProvider
from shared.ai.ai_config import AIConfig
from shared.utils.logger import app_logger

class OpenAIProvider(BaseAIProvider):
    def __init__(self):
        self.name = "openai"
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            app_logger.error("OPENAI_API_KEY environment variable is not set.")
            raise ValueError("OPENAI_API_KEY environment variable is not set.")
        self.url = "https://api.openai.com/v1/chat/completions"

    def generate(self, prompt: str, config: AIConfig = None) -> str:
        if not prompt:
            raise ValueError("Prompt cannot be empty.")
        
        if config is None:
            config = AIConfig()
            
        request_data = {
            "model": config.model if config.model else "gpt-4o-mini",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": config.temperature if config.temperature is not None else 0.2
        }
        
        if config.max_tokens is not None:
            request_data["max_tokens"] = config.max_tokens
        if config.top_p is not None:
            request_data["top_p"] = config.top_p
        
        try:
            app_logger.info(f"Sending request to OpenAI API with model: {request_data['model']}")
            response = requests.post(
                self.url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json=request_data,
                timeout=30
            )
            
            response.raise_for_status()
            data = response.json()
            
            if "choices" not in data or not data["choices"]:
                app_logger.error(f"Unexpected OpenAI API response format: {data}")
                raise Exception(f"Unexpected OpenAI API response format: {data}")
                
            return data["choices"][0]["message"]["content"]
            
        except requests.exceptions.RequestException as e:
            app_logger.error(f"OpenAI API request failed: {str(e)}")
            raise Exception(f"OpenAI API request failed: {str(e)}")
        except (KeyError, IndexError, ValueError) as e:
            app_logger.error(f"Failed to parse OpenAI response: {str(e)}")
            raise Exception(f"Failed to parse OpenAI response: {str(e)}")

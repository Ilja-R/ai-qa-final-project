import json
from .base_masker import BaseMasker
from shared.ai.provider_factory import get_provider
from shared.ai.models import AIConfig


class AIMasker(BaseMasker):
    def __init__(self, provider_name: str):
        self.provider = get_provider(provider_name)
        
    def get_provider_name(self) -> str:
        return self.provider.name

    def mask(self, text: str) -> dict:
        with open("prompts/1_mask_prompt.txt") as f:
            template = f.read()

        prompt = template.replace("{{TEXT}}", text)

        config = AIConfig()

        response = self.provider.generate(prompt, config)
        
        # Remove ```json ... ``` if present
        response = response.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(response)
        except Exception:
            # fallback if AI breaks format
            return {
                "masked_text": text,
                "detected_pii": [],
                "error": "Invalid AI response format"
            }
import json
from shared.ai.provider_factory import get_provider
from shared.ai.models import AIConfig


class CodeReviewer:
    def __init__(self, provider_name: str):
        self.provider = get_provider(provider_name)

    def review(self, code: str, ai_config: AIConfig = None) -> dict:
        prompt = self._build_prompt(code)
        if ai_config is None:
            ai_config = AIConfig(temperature=0.2)

        response = self.provider.generate(prompt, ai_config)

        if response.startswith("```json"):
            response = response.replace("```json", "").replace("```", "").strip()

        return self._parse_response(response)

    def _build_prompt(self, code: str) -> str:
        with open("prompts/4_code_review_prompt.txt", encoding='utf-8') as f:
            template = f.read()

        return template.replace("{{CODE}}", code)

    def _parse_response(self, response: str):
        try:
            return json.loads(response)
        except Exception as e:
            return {
                "summary": "Error parsing AI response",
                "critical_issues": [],
                "suggestions": [],
                "positive_observations": [],
                "overall_score": 0,
                "error": str(e),
                "raw": response
            }

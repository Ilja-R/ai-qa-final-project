import json
from shared.ai.provider_factory import get_provider
from shared.ai.ai_config import AIConfig


class BugReporter:
    def __init__(self, provider_name: str):
        self.provider = get_provider(provider_name)

    def generate_report(self, checklist: str, scenarios: str, review: str, tests: str, ai_config: AIConfig = None) -> dict:
        prompt = self._build_prompt(checklist, scenarios, review, tests)
        if ai_config is None:
            ai_config = AIConfig()

        response = self.provider.generate(prompt, ai_config)

        if response.startswith("```json"):
            response = response.replace("```json", "").replace("```", "").strip()

        return self._parse_response(response)

    def _build_prompt(self, checklist: str, scenarios: str, review: str, tests: str) -> str:
        with open("prompts/5_bug_report.txt", encoding='utf-8') as f:
            template = f.read()

        return template.replace("{{CHECKLIST}}", checklist)\
                       .replace("{{SCENARIOS}}", scenarios)\
                       .replace("{{REVIEW}}", review)\
                       .replace("{{TESTS}}", tests)

    def _parse_response(self, response: str):
        try:
            return json.loads(response)
        except Exception as e:
            return {
                "status": "ERROR",
                "message": "Error parsing AI response",
                "error": str(e),
                "raw": response
            }

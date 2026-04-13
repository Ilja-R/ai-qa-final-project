import json
from shared.ai.provider_factory import get_provider
from shared.ai.models import AIConfig


class ScenarioGenerator:

    def __init__(self, provider_name: str):
        self.provider = get_provider(provider_name)

    def generate(self, checklist_text: str, variables: dict, locators: dict, ai_config: AIConfig = None) -> dict:
        prompt = self._build_prompt(checklist_text, variables, locators)
        if ai_config is None:
            ai_config = AIConfig()

        response = self.provider.generate(prompt, ai_config)

        if response.startswith("```json"):
            response = response.replace("```json", "").replace("```", "").strip()
            
        print(f"AI scenario response: {response}")  # Debug log
        
        return self._parse_response(response)

    def _build_prompt(self, checklist_text: str, variables: dict, locators: dict) -> str:
        with open("prompts/2_scenario_prompt.txt") as f:
            template = f.read()

        variables_str = json.dumps(variables, indent=2)
        locators_str = json.dumps(locators, indent=2)

        return template.replace("{{CHECKLIST}}", checklist_text)\
                       .replace("{{VARIABLES}}", variables_str)\
                       .replace("{{LOCATORS}}", locators_str)\

    def _parse_response(self, response: str):
        try:
            return json.loads(response)
        except Exception:
            return {
                "scenarios": [],
                "error": "Invalid AI response format",
                "raw": response
            }
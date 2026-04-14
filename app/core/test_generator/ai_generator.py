import json
from shared.ai.provider_factory import get_provider
from shared.ai.ai_config import AIConfig


class PlaywrightAIGenerator:

    def __init__(self, provider_name: str):
        self.provider = get_provider(provider_name)

    def generate(self, scenarios: dict, variables: dict, locators: dict, config: dict = None):
        prompt = self._build_prompt(scenarios, variables, locators)

        if not config:
            config = AIConfig(
                temperature=0.2,
            )

        response = self.provider.generate(prompt, config)

        return {
            "files": [
                {
                    "path": "tests/generated.spec.ts",
                    "content": response
                }
            ]
        }

    def _build_prompt(self, scenarios, variables, locators):
        with open("prompts/3_playwright_prompt.txt") as f:
            template = f.read()

        return template\
            .replace("{{VARIABLES}}", json.dumps(variables, indent=2))\
            .replace("{{LOCATORS}}", json.dumps(locators, indent=2))\
            .replace("{{SCENARIOS}}", json.dumps(scenarios, indent=2))
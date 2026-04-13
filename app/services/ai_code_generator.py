
from services.test_generator.ai_generator import PlaywrightAIGenerator


class AICodeGenerator:

    def generate_code(self, scenarios, variables, locators, provider="mistral"):
        ai_code_generator = PlaywrightAIGenerator(provider)
        return ai_code_generator.generate(scenarios, variables, locators)
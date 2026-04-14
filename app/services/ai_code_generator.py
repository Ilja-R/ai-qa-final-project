from app.core.test_generator.ai_generator import PlaywrightAIGenerator
from shared.utils.logger import app_logger

class AICodeGenerator:
    def generate_code(self, scenarios, variables, locators, provider="mistral"):
        app_logger.info(f"Starting Playwright code generation with provider: {provider}")
        ai_code_generator = PlaywrightAIGenerator(provider)
        result = ai_code_generator.generate(scenarios, variables, locators)
        app_logger.info("Successfully generated Playwright test code")
        return result

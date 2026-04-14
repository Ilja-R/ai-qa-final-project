from app.core.scenario_generator.generator import ScenarioGenerator
from shared.utils.logger import app_logger

class ScenarioGeneratorService:
    def generate_test_scenarios(self, checklist_text: str, variables: dict, locators: dict, ai_config: dict = None, provider: str = "mistral") -> dict:
        app_logger.info(f"Starting scenario generation with provider: {provider}")
        generator = ScenarioGenerator(provider)
        result = generator.generate(checklist_text, variables, locators, ai_config)
        app_logger.info(f"Successfully generated {len(result.get('scenarios', []))} scenarios")
        return result

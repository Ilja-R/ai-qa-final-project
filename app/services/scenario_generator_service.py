from services.scenario_generator.generator import ScenarioGenerator

class ScenarioGeneratorService:
    
    def generate_scenarios(self, checklist_text: str, variables: dict, locators: dict, ai_config: dict = None, provider: str = "mistral") -> dict:
        generator = ScenarioGenerator(provider)
        return generator.generate(checklist_text, variables, locators, ai_config)
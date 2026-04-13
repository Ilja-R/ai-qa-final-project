from services.scenario_generator.generator import ScenarioGenerator

class GeneratorService:
    
    def generate_scenarios(self, jira_text: str, variables: dict, locators: dict, ai_config: dict = None, provider: str = "mistral") -> dict:
        generator = ScenarioGenerator(provider)
        return generator.generate(jira_text, variables, locators, ai_config)
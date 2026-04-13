from abc import ABC, abstractmethod
from shared.ai.ai_config import AIConfig

class BaseAIProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, config: AIConfig) -> str:
        pass
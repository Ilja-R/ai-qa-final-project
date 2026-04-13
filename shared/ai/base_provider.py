from abc import ABC, abstractmethod
from shared.ai.models import AIConfig

class BaseAIProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, config: AIConfig) -> str:
        pass
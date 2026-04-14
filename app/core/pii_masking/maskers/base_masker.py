from abc import ABC, abstractmethod

class BaseMasker(ABC):
    @abstractmethod
    def mask(self, text: str) -> str:
        pass
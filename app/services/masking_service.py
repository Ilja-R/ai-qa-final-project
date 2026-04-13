from services.pii_masking.maskers.simple_masker import SimpleMasker
from services.pii_masking.maskers.ai_masker import AIMasker


class MaskingService:

    def mask(self, text: str, mode: str, provider: str):
        if mode == "simple":
            masker = SimpleMasker()
        elif mode == "ai":
            masker = AIMasker(provider)
        else:
            raise ValueError(f"Unknown masking mode: {mode}")

        return masker.mask(text)
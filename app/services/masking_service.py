from app.core.pii_masking.maskers.ai_masker import AIMasker
from app.core.pii_masking.maskers.simple_masker import SimpleMasker
from shared.utils.logger import app_logger

class MaskingService:
    def mask(self, content: str, mode: str = "simple", provider: str = "mistral"):
        app_logger.info(f"Starting PII masking in mode: {mode}")
        if mode == "ai":
            masker = AIMasker(provider)
        else:
            masker = SimpleMasker()
            
        result = masker.mask(content)
        app_logger.info("PII masking completed")
        return result

from services.code_reviewer.reviewer import CodeReviewer
from shared.ai.models import AIConfig
from shared.utils.logger import app_logger

class CodeReviewService:
    def review_code(self, code: str, ai_config: AIConfig = None, provider: str = "mistral") -> dict:
        app_logger.info(f"Starting code review with provider: {provider}")
        reviewer = CodeReviewer(provider)
        result = reviewer.review(code, ai_config)
        app_logger.info("Code review completed")
        return result

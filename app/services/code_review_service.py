from services.code_reviewer.reviewer import CodeReviewer

class CodeReviewService:
    def review_code(self, code: str, provider: str = "mistral") -> dict:
        reviewer = CodeReviewer(provider)
        return reviewer.review(code)

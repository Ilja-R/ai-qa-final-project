from fastapi import APIRouter
from app.services.code_review_service import CodeReviewService
from shared.contracts.models import CodeReviewRequest, CodeReviewResponse

router = APIRouter(prefix="/review", tags=["Code Review"])

@router.post("/run", response_model=CodeReviewResponse)
def review_code(req: CodeReviewRequest):
    review_service = CodeReviewService()
    result = review_service.review_code(
        code=req.code,
        context=req.context,
        provider=req.provider
    )
    return CodeReviewResponse(**result)

from fastapi import APIRouter
from app.services.masking_service import MaskingService
from shared.contracts.models import MaskingRequest, MaskingResponse

router = APIRouter(prefix="/masking", tags=["Masking"])

@router.post("/mask", response_model=MaskingResponse)
def mask_content(req: MaskingRequest):
    masking_service = MaskingService()
    result = masking_service.mask(
        req.content,
        req.mode,
        req.provider
    )
    return MaskingResponse(masked_text=result.get("masked_text", ""))

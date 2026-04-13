from fastapi import APIRouter
from app.services.bug_report_service import BugReportService
from shared.contracts.models import BugReportRequest, BugReportResponse

router = APIRouter(prefix="/bugs", tags=["Bug Reporting"])

@router.post("/report", response_model=BugReportResponse)
def generate_bug_report(req: BugReportRequest):
    bug_report_service = BugReportService()
    result = bug_report_service.generate_report(
        checklist=req.checklist,
        scenarios=req.scenarios,
        review=req.review,
        tests=req.tests,
        provider=req.provider
    )
    return BugReportResponse(**result)

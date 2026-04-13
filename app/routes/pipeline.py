from fastapi import APIRouter
from app.services.ai_code_generator import AICodeGenerator
from app.services.file_writer_service import FileWriterService
from app.services.masking_service import MaskingService
from app.services.scenario_generator_service import ScenarioGeneratorService
from app.services.code_review_service import CodeReviewService
from app.services.bug_report_service import BugReportService
from shared.contracts.models import BaseAIRequest
from pydantic import BaseModel
from typing import Dict, Any, Optional
from shared.utils.logger import app_logger
from shared.utils.artifact_exporter import exporter

router = APIRouter(tags=["Pipeline"])

class PipelineRequest(BaseAIRequest):
    checklist: Dict[str, Any]
    variables: Dict[str, Any]
    page_locators: Dict[str, Any]

@router.post("/pipeline/run")
def run_pipeline(req: PipelineRequest):
    app_logger.info("--- Starting E2E QA Pipeline Run ---")
    
    # Configuration extraction
    masking_config = req.config.get("piiMasking", {}) if req.config else {}
    mode = masking_config.get("mode", "simple")
    provider = req.provider

    # 1. Masking
    masking_service = MaskingService()
    masking_result = masking_service.mask(
        req.checklist.get("content", ""),
        mode,
        provider
    )
    exporter.save_artifact("1_masking_result", masking_result)
    
    masked_content = masking_result.get("masked_text", "")
    
    # 2. Scenario Generation
    generator_service = ScenarioGeneratorService()
    scenarios_result = generator_service.generate_test_scenarios(
        checklist_text=masked_content,
        variables=req.variables,
        locators=req.page_locators,
        provider=provider
    )
    scenarios = scenarios_result.get("scenarios", [])
    exporter.save_artifact("2_scenarios", scenarios)
    
    # 3. Code Generation
    ai_code_generator = AICodeGenerator()
    code_result = ai_code_generator.generate_code(
        scenarios=scenarios,
        variables=req.variables,
        locators=req.page_locators,
        provider=provider
    )
    generated_code = code_result.get("files", [])
    exporter.save_artifact("3_generated_code", generated_code)
    
    # 4. File Writing
    file_writer_service = FileWriterService()
    file_writer_service.write_to_file(generated_code)

    # 5. Optional: Code Review (If there is code)
    review_result = None
    if generated_code:
        review_service = CodeReviewService()
        combined_code = "\n\n".join([f"File: {f['path']}\n{f['content']}" for f in generated_code])
        review_result = review_service.review_code(
            code=combined_code,
            provider=provider
        )
        exporter.save_artifact("4_code_review", review_result)

    # 6. Optional: Bug Report
    bug_report = None
    if review_result:
        bug_report_service = BugReportService()
        bug_report = bug_report_service.generate_report(
            checklist=masked_content,
            scenarios=str(scenarios),
            review=str(review_result),
            tests=str(generated_code),
            provider=provider
        )
        exporter.save_artifact("5_bug_report", bug_report)

    app_logger.info("--- E2E QA Pipeline Run Completed Successfully ---")
    
    return {
        "masking": masking_result,
        "scenarios": scenarios,
        "generated_code": generated_code,
        "code_review": review_result,
        "bug_report": bug_report
    }

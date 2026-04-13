from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_code_generator import AICodeGenerator
from app.services.file_writer_service import FileWriterService
from app.services.masking_service import MaskingService
from app.services.generator_service import GeneratorService

router = APIRouter()

class PipelineRequest(BaseModel):
    checklist: dict
    variables: dict
    page_locators: dict
    config: dict


@router.post("/pipeline/run")
def run_pipeline(req: PipelineRequest):
    masking_service = MaskingService()
    
    request_data = {
        "checklist": req.checklist,
        "variables": req.variables,
        "page_locators": req.page_locators,
        "config": req.config
    }

    masking_config = request_data["config"].get("piiMasking", {})
    mode = masking_config.get("mode", "simple")
    provider = request_data["config"].get("aiProvider", "mistral")

    masking_result = masking_service.mask(
        req.checklist.get("content", ""),
        mode,
        provider
    )
    
    request_data["checklist"]["masked_content"] = masking_result.get("masked_text", "")
    
    generator_service = GeneratorService()
    scenarios = generator_service.generate_scenarios(
        checklist_text=request_data["checklist"]["masked_content"],
        variables=request_data["variables"],
        locators=request_data["page_locators"],
        provider=provider
    )
    request_data["scenarios"] = scenarios.get("scenarios", [])
    
    ai_code_generator = AICodeGenerator()
    code = ai_code_generator.generate_code(
        scenarios=request_data["scenarios"],
        variables=request_data["variables"],
        locators=request_data["page_locators"],
        provider=provider
    )
    request_data["generated_code"] = code
    
    file_writer_service = FileWriterService()
    file_writer_service.write_to_file(code.get("files", []))

    return request_data
from fastapi import APIRouter
from app.services.ai_code_generator import AICodeGenerator
from app.services.file_writer_service import FileWriterService
from shared.contracts.models import CodeGenRequest, CodeGenResponse

router = APIRouter(prefix="/code", tags=["Code Generation"])

@router.post("/generate", response_model=CodeGenResponse)
def generate_code(req: CodeGenRequest):
    ai_code_generator = AICodeGenerator()
    # Convert scenarios to dict if needed by service
    scenarios_dict = [s.model_dump() for s in req.scenarios]
    
    result = ai_code_generator.generate_code(
        scenarios=scenarios_dict,
        variables=req.variables,
        locators=req.locators,
        provider=req.provider
    )
    
    # Optional: Write to file as side effect
    file_writer_service = FileWriterService()
    file_writer_service.write_to_file(result.get("files", []))
    
    return CodeGenResponse(files=result.get("files", []))

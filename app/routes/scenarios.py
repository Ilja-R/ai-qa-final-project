from fastapi import APIRouter
from app.services.scenario_generator_service import ScenarioGeneratorService
from shared.contracts.models import ScenarioRequest, ScenarioResponse

router = APIRouter(prefix="/scenarios", tags=["Scenarios"])

@router.post("/generate", response_model=ScenarioResponse)
def generate_test_scenarios(req: ScenarioRequest):
    generator_service = ScenarioGeneratorService()
    result = generator_service.generate_test_scenarios(
        checklist_text=req.checklist_text,
        variables=req.variables,
        locators=req.locators,
        provider=req.provider
    )
    return ScenarioResponse(scenarios=result.get("scenarios", []), raw=result.get("raw"))

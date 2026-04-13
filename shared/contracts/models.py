from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class BaseAIRequest(BaseModel):
    provider: str = "mistral"
    config: Optional[Dict[str, Any]] = None

class MaskingRequest(BaseAIRequest):
    content: str
    mode: str = "simple"

class MaskingResponse(BaseModel):
    masked_text: str
    metadata: Optional[Dict[str, Any]] = None

class ScenarioRequest(BaseAIRequest):
    checklist_text: str
    variables: Dict[str, Any]
    locators: Dict[str, Any]

class ScenarioStep(BaseModel):
    step: str
    expected: str

class Scenario(BaseModel):
    name: str
    steps: List[ScenarioStep]

class ScenarioResponse(BaseModel):
    scenarios: List[Scenario]
    raw: Optional[str] = None

class CodeGenRequest(BaseAIRequest):
    scenarios: List[Scenario]
    variables: Dict[str, Any]
    locators: Dict[str, Any]

class FileContent(BaseModel):
    path: str
    content: str

class CodeGenResponse(BaseModel):
    files: List[FileContent]

class CodeReviewRequest(BaseAIRequest):
    code: str
    context: Optional[str] = ""

class CodeReviewIssue(BaseModel):
    file: str
    line: int
    issue: str
    suggestion: str

class CodeReviewResponse(BaseModel):
    summary: str
    critical_issues: List[CodeReviewIssue]
    suggestions: List[CodeReviewIssue]
    positive_observations: List[str]
    overall_score: int

class BugReportRequest(BaseAIRequest):
    checklist: str
    scenarios: str
    review: str
    tests: str

class BugReportResponse(BaseModel):
    status: Optional[str] = None
    title: Optional[str] = None
    severity: Optional[str] = None
    priority: Optional[str] = None
    environment: Optional[str] = "SauceDemo web"
    preconditions: Optional[str] = None
    steps_to_reproduce: Optional[List[str]] = []
    actual_result: Optional[str] = None
    expected_result: Optional[str] = None
    probable_root_cause: Optional[str] = None
    evidence: Optional[str] = None

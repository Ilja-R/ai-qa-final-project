from fastapi import APIRouter
import os
from typing import List, Dict

router = APIRouter(tags=["Config"])

@router.get("/config/models")
def get_available_models():
    """
    Checks environment variables for API keys and returns a list of available providers and their models.
    """
    available_providers = []
    
    if os.getenv("GEMINI_API_KEY"):
        available_providers.append({
            "id": "gemini",
            "name": "Google Gemini",
            "models": ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-3-flash-preview"]
        })
        
    if os.getenv("MISTRAL_API_KEY"):
        available_providers.append({
            "id": "mistral",
            "name": "Mistral AI",
            "models": ["mistral-small", "mistral-medium", "mistral-large-latest"]
        })
        
    if os.getenv("OPENAI_API_KEY"):
        available_providers.append({
            "id": "openai",
            "name": "OpenAI",
            "models": ["gpt-4o-mini", "gpt-4o"]
        })
        
    return {"providers": available_providers}

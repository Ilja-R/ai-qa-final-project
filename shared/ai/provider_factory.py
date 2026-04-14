from shared.ai.mistral_provider import MistralProvider
from shared.ai.gemini_provider import GeminiProvider
from shared.ai.openai_provider import OpenAIProvider

_providers = {
    "mistral": MistralProvider,
    "gemini": GeminiProvider,
    "openai": OpenAIProvider
}

def get_provider(name: str):
    provider_class = _providers.get(name.lower())
    if provider_class:
        return provider_class()

    raise Exception(f"Unsupported provider: {name}")
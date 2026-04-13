from shared.ai.mistral_provider import MistralProvider
from shared.ai.gemini_provider import GeminiProvider

def get_provider(name: str):
    if name == "mistral":
        return MistralProvider()
    if name == "gemini":
        return GeminiProvider()

    raise Exception(f"Unsupported provider: {name}")
from shared.ai.mistral_provider import MistralProvider

def get_provider(name: str):
    if name == "mistral":
        return MistralProvider()

    raise Exception(f"Unsupported provider: {name}")
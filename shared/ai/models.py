from dataclasses import dataclass
from typing import Optional

@dataclass
class AIConfig:
    model: str = "mistral-small"
    temperature: float = 0.2
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
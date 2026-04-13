from dataclasses import dataclass
from typing import List


@dataclass
class TestStep:
    step: str
    expected: str


@dataclass
class TestScenario:
    name: str
    steps: List[TestStep]


@dataclass
class ScenarioResponse:
    scenarios: List[TestScenario]
from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.enums import Decision
from app.models import Application


@dataclass(frozen=True)
class EvaluationResult:
    decision: Decision
    reasons: list[str]


class CreditPolicy(ABC):
    @abstractmethod
    def evaluate(self, application: Application) -> EvaluationResult:
        raise NotImplementedError

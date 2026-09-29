from app.enums import Decision
from app.models import Application
from app.strategies.base import CreditPolicy, EvaluationResult


class CardPolicy(CreditPolicy):
    def evaluate(self, application: Application) -> EvaluationResult:
        score = application.external_score
        income = application.monthly_income

        approved = score >= 550 or (
            score >= 500 and income >= 3_000_000
        )

        reasons: list[str] = []

        if not approved:
            reasons.append(
                "Application does not meet the CARD score/income criteria."
            )

        return EvaluationResult(
            decision=(
                Decision.APPROVED
                if approved
                else Decision.REJECTED
            ),
            reasons=reasons,
        )

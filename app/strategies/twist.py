from app.enums import Decision
from app.models import Application
from app.strategies.base import CreditPolicy, EvaluationResult


class TwistPolicy(CreditPolicy):
    def evaluate(self, application: Application) -> EvaluationResult:
        reasons: list[str] = []

        if application.external_score < 600:
            reasons.append("External score must be at least 600.")

        monthly_payment = application.amount / 12
        max_payment = application.monthly_income * 0.35

        if monthly_payment > max_payment:
            reasons.append(
                "Monthly payment exceeds 35% of monthly income."
            )

        return EvaluationResult(
            decision=(
                Decision.REJECTED
                if reasons
                else Decision.APPROVED
            ),
            reasons=reasons,
        )

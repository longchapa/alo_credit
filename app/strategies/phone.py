from app.enums import Decision
from app.models import Application
from app.strategies.base import CreditPolicy, EvaluationResult


class PhonePolicy(CreditPolicy):
    def evaluate(self, application: Application) -> EvaluationResult:
        reasons: list[str] = []

        if application.external_score < 700:
            reasons.append("External score must be at least 700.")

        if application.employment_months < 12:
            reasons.append("Employment must be at least 12 months.")

        monthly_payment = application.amount / 12
        max_payment = application.monthly_income * 0.25

        if monthly_payment > max_payment:
            reasons.append(
                "Monthly payment exceeds 25% of monthly income."
            )

        return EvaluationResult(
            decision=(
                Decision.REJECTED
                if reasons
                else Decision.APPROVED
            ),
            reasons=reasons,
        )

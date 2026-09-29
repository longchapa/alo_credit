from app.enums import Decision
from app.models import Application
from app.strategies.base import CreditPolicy, EvaluationResult


class CardPolicy(CreditPolicy):
    def evaluate(self, application: Application) -> EvaluationResult:
        reasons: list[str] = []

        # I change the criteria for CARD because an user with a higher score and low income in previous criteria can get a card.        
        if application.external_score < 500:
                    reasons.append("External score must be at least 500.")
                    
        if application.monthly_income < 3_000_000:
                    reasons.append("Monthly income must be at least 3,000,000.")



        return EvaluationResult(
            decision=(
                Decision.REJECTED
                if reasons
                else Decision.APPROVED
            ),
            reasons=reasons,
        )

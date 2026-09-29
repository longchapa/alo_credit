from app.enums import Decision
from app.models import Application
from app.repositories.application_repository import ApplicationRepository
from app.schemas import ApplicationCreate
from app.strategies.resolver import PolicyResolver


class ApplicationService:
    def __init__(
        self,
        repository: ApplicationRepository,
        policy_resolver: PolicyResolver,
    ) -> None:
        self.repository = repository
        self.policy_resolver = policy_resolver

    def create_application(
        self,
        data: ApplicationCreate,
    ) -> Application:
        application = Application(
            amount=data.amount,
            monthly_income=data.monthly_income,
            employment_months=data.employment_months,
            external_score=data.external_score,
            product=data.product,
            decision=Decision.REJECTED,
            rejection_reasons=[],
        )

        policy = self.policy_resolver.resolve(application.product)
        result = policy.evaluate(application)

        application.decision = result.decision
        application.rejection_reasons = result.reasons

        return self.repository.create(application)

    def reevaluate(self, application_id: int) -> Application:
        application = self.repository.get_by_id(application_id)

        if application is None:
            raise LookupError("Application not found.")

        policy = self.policy_resolver.resolve(application.product)
        result = policy.evaluate(application)

        application.decision = result.decision
        application.rejection_reasons = result.reasons

        return self.repository.update(application)
    
    def get_application_by_id(self, application_id: int) -> Application:
        application = self.repository.get_by_id(application_id)

        if application is None:
            raise LookupError("Application not found.")

        return application
    
    def list_applications(self, status: Decision | None = None, product: str | None = None) -> list[Application]:
        return self.repository.list_applications(status=status, product=product)

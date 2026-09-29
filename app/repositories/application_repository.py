from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Application


class ApplicationRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, application: Application) -> Application:
        self.db.add(application)
        self.db.commit()
        self.db.refresh(application)
        return application

    def get_by_id(self, application_id: int) -> Application | None:
        return self.db.scalar(
            select(Application).where(Application.id == application_id)
        )

    def update(self, application: Application) -> Application:
        self.db.commit()
        self.db.refresh(application)
        return application
    
    def list_applications(
        self,
        status: str | None = None,
        product: str | None = None,
    ) -> list[Application]:
        query = select(Application)

        if status:
            query = query.where(Application.decision == status)

        if product:
            query = query.where(Application.product == product)

        return self.db.scalars(query).all()

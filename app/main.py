from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.repositories.application_repository import ApplicationRepository
from app.schemas import ApplicationCreate, ApplicationResponse
from app.services.application_service import ApplicationService
from app.strategies.resolver import PolicyResolver
from app.enums import Decision, Product

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Senior Python Backend Challenge")


def get_application_service(
    db: Session = Depends(get_db),
) -> ApplicationService:
    return ApplicationService(
        repository=ApplicationRepository(db),
        policy_resolver=PolicyResolver(),
    )


@app.get("/applications/{id}", response_model=ApplicationResponse)
def get_application_by_id(
    id: int,
    service: ApplicationService = Depends(get_application_service),
):
    try:
        return service.get_application_by_id(id)
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    

@app.get("/applications", response_model=list[ApplicationResponse])
def list_applications(
    status: Decision | None = None,
    product: Product | None = None,
    service: ApplicationService = Depends(get_application_service)
):
    return service.list_applications(status=status, product=product)


@app.post(
    "/applications",
    response_model=ApplicationResponse,
    status_code=201,
)
def create_application(
    data: ApplicationCreate,
    service: ApplicationService = Depends(get_application_service),
):
    print(f"Received application data: {data}")
    return service.create_application(data)


@app.post(
    "/applications/{application_id}/reevaluate",
    response_model=ApplicationResponse,
)
def reevaluate_application(
    application_id: int,
    service: ApplicationService = Depends(get_application_service),
):
    try:
        return service.reevaluate(application_id)
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

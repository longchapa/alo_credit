from pydantic import BaseModel, ConfigDict, Field

from app.enums import Decision, Product


class ApplicationCreate(BaseModel):
    amount: int = Field(gt=0)
    monthly_income: int = Field(gt=0)
    employment_months: int = Field(ge=0)
    external_score: int = Field(ge=0, le=1000)
    product: Product


class ApplicationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    amount: int
    monthly_income: int
    employment_months: int
    external_score: int
    product: Product
    decision: Decision
    rejection_reasons: list[str]

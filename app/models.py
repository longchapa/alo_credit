from sqlalchemy import JSON, Enum as SQLEnum, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.enums import Decision, Product


class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    monthly_income: Mapped[int] = mapped_column(Integer, nullable=False)
    employment_months: Mapped[int] = mapped_column(Integer, nullable=False)
    external_score: Mapped[int] = mapped_column(Integer, nullable=False)
    product: Mapped[Product] = mapped_column(
        SQLEnum(Product),
        nullable=False,
    )
    decision: Mapped[Decision] = mapped_column(
        SQLEnum(Decision),
        nullable=False,
    )
    rejection_reasons: Mapped[list[str]] = mapped_column(
        JSON,
        nullable=False,
        default=list,
    )

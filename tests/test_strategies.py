from app.enums import Decision, Product
from app.models import Application
from app.strategies.card import CardPolicy
from app.strategies.phone import PhonePolicy
from app.strategies.twist import TwistPolicy


def make_application(**overrides):
    data = {
        "amount": 1_000_000,
        "monthly_income": 5_000_000,
        "employment_months": 24,
        "external_score": 750,
        "product": Product.PHONE,
        "decision": Decision.REJECTED,
        "rejection_reasons": [],
    }
    data.update(overrides)
    return Application(**data)


def test_phone_approved():
    result = PhonePolicy().evaluate(make_application())
    assert result.decision == Decision.APPROVED
    assert result.reasons == []


def test_phone_rejected():
    result = PhonePolicy().evaluate(
        make_application(
            external_score=650,
            employment_months=6,
            amount=20_000_000,
        )
    )
    assert result.decision == Decision.REJECTED
    assert len(result.reasons) == 3


def test_twist_approved():
    result = TwistPolicy().evaluate(
        make_application(
            product=Product.TWIST,
            external_score=650,
            amount=10_000_000,
            monthly_income=4_000_000,
        )
    )
    assert result.decision == Decision.APPROVED


def test_twist_rejected():
    result = TwistPolicy().evaluate(
        make_application(
            product=Product.TWIST,
            external_score=550,
        )
    )
    assert result.decision == Decision.REJECTED


def test_card_approved_by_score():
    result = CardPolicy().evaluate(
        make_application(
            product=Product.CARD,
            external_score=550,
        )
    )
    assert result.decision == Decision.APPROVED


def test_card_approved_by_income_exception():
    result = CardPolicy().evaluate(
        make_application(
            product=Product.CARD,
            external_score=500,
            monthly_income=3_000_000,
        )
    )
    assert result.decision == Decision.APPROVED


def test_card_rejected():
    result = CardPolicy().evaluate(
        make_application(
            product=Product.CARD,
            external_score=499,
            monthly_income=2_999_999,
        )
    )
    assert result.decision == Decision.REJECTED

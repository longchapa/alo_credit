from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_application_e2e():
    response = client.post(
        "/applications",
        json={
            "amount": 1_000_000,
            "monthly_income": 5_000_000,
            "employment_months": 24,
            "external_score": 750,
            "product": "PHONE",
        },
    )

    assert response.status_code == 201

    body = response.json()
    assert body["decision"] == "APPROVED"
    assert body["rejection_reasons"] == []
    assert body["product"] == "PHONE"


def test_create_rejected_application():
    response = client.post(
        "/applications",
        json={
            "amount": 20_000_000,
            "monthly_income": 2_000_000,
            "employment_months": 6,
            "external_score": 650,
            "product": "PHONE",
        },
    )

    assert response.status_code == 201

    body = response.json()
    assert body["decision"] == "REJECTED"
    assert len(body["rejection_reasons"]) == 3


def test_invalid_input():
    response = client.post(
        "/applications",
        json={
            "amount": -1,
            "monthly_income": 2_000_000,
            "employment_months": 12,
            "external_score": 700,
            "product": "PHONE",
        },
    )

    assert response.status_code == 422

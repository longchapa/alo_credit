# Prueba Backend Senior Python — solución de estudio

Proyecto de referencia para estudiar una posible solución a la prueba de Alo Credit.
La implementación prioriza claridad, separación de responsabilidades y facilidad para defender las decisiones en entrevista.

## Stack
- Python 3.11+
- FastAPI
- SQLAlchemy 2.x
- Pydantic v2
- SQLite para ejecución local sencilla
- pytest

## Estructura

```text
app/
  main.py
  database.py
  enums.py
  models.py
  schemas.py
  repositories/
    application_repository.py
  services/
    application_service.py
  strategies/
    base.py
    card.py
    phone.py
    twist.py
    resolver.py
tests/
  test_strategies.py
  test_api.py
requirements.txt
Dockerfile
docker-compose.yml
```

## Ejecutar

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger: http://localhost:8000/docs

Tests:

```bash
pytest -q
```

## Nota

Esta es una solución de estudio deliberadamente pequeña. No intenta implementar Clean Architecture/Hexagonal completa ni agregar infraestructura innecesaria. Se siguio el scafolding del repositorio dando como resultado un acercamiento a arquitectura por capas

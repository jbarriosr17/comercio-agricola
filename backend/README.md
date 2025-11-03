
# Backend (FastAPI)

## Endpoints
- `GET /health` — salud del servicio
- `GET /api/v1/products` — lista de productos
- `POST /api/v1/orders` — crea un pedido

## Variables
- `DATABASE_URL` (opcional). Por defecto usa SQLite: `sqlite:///./app.db`.

## Ejecutar
```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

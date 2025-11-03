
import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_list_products():
    r = client.get("/api/v1/products")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert {"id","name","category","price","stock"}.issubset(data[0].keys())

def test_create_order_ok():
    # tomar dos productos existentes
    products = client.get("/api/v1/products").json()
    payload = {
        "customer_name": "Cliente Demo",
        "items": [
            {"product_id": products[0]["id"], "quantity": 1}
        ]
    }
    r = client.post("/api/v1/orders", json=payload)
    assert r.status_code == 201
    assert "id" in r.json()

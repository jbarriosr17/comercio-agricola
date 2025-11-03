
from fastapi import FastAPI
from .db import Base, engine, SessionLocal
from .models import Product
from .routers import products, orders

app = FastAPI(title="Comercio Agrícola API", version="1.0.0")

# Crear tablas y datos semilla mínimos
Base.metadata.create_all(bind=engine)
with SessionLocal() as db:
    if db.query(Product).count() == 0:
        db.add_all([
            Product(name="Maíz blanco quintal", category="Granos", price=180.0, stock=50),
            Product(name="Frijol negro quintal", category="Granos", price=400.0, stock=30),
            Product(name="Fertilizante NPK 15-15-15 (50kg)", category="Insumos", price=320.0, stock=100),
        ])
        db.commit()

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(products.router)
app.include_router(orders.router)

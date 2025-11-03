
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import Product, Order, OrderItem
from ..schemas import OrderIn, OrderOut

router = APIRouter(prefix="/api/v1/orders", tags=["orders"])

@router.post("", response_model=OrderOut, status_code=201)
def create_order(payload: OrderIn, db: Session = Depends(get_db)):
    # Validar existencia de productos y stock
    products = {p.id: p for p in db.query(Product).filter(Product.id.in_([i.product_id for i in payload.items])).all()}
    if len(products) != len(payload.items):
        raise HTTPException(status_code=400, detail="Uno o más productos no existen")

    # Verificar stock
    for item in payload.items:
        if products[item.product_id].stock < item.quantity:
            raise HTTPException(status_code=409, detail=f"Sin stock suficiente para producto {item.product_id}")

    # Crear pedido y disminuir stock
    order = Order(customer_name=payload.customer_name)
    db.add(order)
    db.flush()  # para obtener ID

    for item in payload.items:
        db.add(OrderItem(order_id=order.id, product_id=item.product_id, quantity=item.quantity))
        products[item.product_id].stock -= item.quantity

    db.commit()
    db.refresh(order)
    return order

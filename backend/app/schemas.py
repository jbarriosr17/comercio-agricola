
from pydantic import BaseModel, Field
from typing import List

class ProductOut(BaseModel):
    id: int
    name: str
    category: str
    price: float
    stock: int
    class Config:
        from_attributes = True

class OrderItemIn(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)

class OrderIn(BaseModel):
    customer_name: str
    items: List[OrderItemIn]

class OrderOut(BaseModel):
    id: int
    class Config:
        from_attributes = True

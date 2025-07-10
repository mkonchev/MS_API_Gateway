from pydantic import BaseModel, Field
from typing import List
from app.order_service.schemas.orderitem import OrderItem


class Order(BaseModel):
    customer: str = Field(default=..., description="Покупатель")
    goods: List[OrderItem] = Field(default=..., description="Товары")
    status: str = Field(default=..., description="Статус заказа")

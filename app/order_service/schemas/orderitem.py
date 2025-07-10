from pydantic import BaseModel, Field


class OrderItem(BaseModel):
    item_id: int = Field(..., description="ID товара")
    quantity: int = Field(1, gt=0, description="Количество товара")
    name: str | None = None
    price: int | None = None
    price_at_order: int | None = None

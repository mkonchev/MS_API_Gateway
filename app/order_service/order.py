import httpx
import os
from fastapi import APIRouter
from dotenv import load_dotenv
from app.order_service.schemas.order import Order

router = APIRouter(prefix="/order", tags=["Order"])


load_dotenv()
ORDER_SERVICE = os.getenv("ORDER_SERVICE")


@router.post("/create")
async def create_order(order: Order):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{ORDER_SERVICE}/orders/",
            json=order.model_dump()
        )
    return response.json()

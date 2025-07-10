import httpx
import os
from fastapi import APIRouter
from dotenv import load_dotenv
from app.order_service.schemas.order import Order

router = APIRouter(prefix="/order", tags=["Order"])


load_dotenv()
ORDER_SERVICE = os.getenv("ORDER_SERVICE")
USER_SERVICE = os.getenv("USER_SERVICE")


@router.post("/create")
async def create_order(token: str, order: Order):
    temp_order = order.model_dump(exclude="customer")

    async def get_email(token: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{USER_SERVICE}/users/me?token={token}"
            )
            user_data = response.json()
        return user_data["email"]

    temp_order["customer"] = await get_email(token)

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{ORDER_SERVICE}/orders/",
            json=temp_order
        )
    return response.json()

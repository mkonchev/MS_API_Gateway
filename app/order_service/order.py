import httpx
from fastapi import APIRouter


router = APIRouter()


ORDER_SERVICE = "http://order"


@router.post("/order/create")
async def craete_order(product_id: int, quantity: int):
    async with httpx.AsyncClient() as client:
        responce = await client.post(
            f"{ORDER_SERVICE}/orders/",
            json={"product_id": product_id, "quantity": quantity}
        )
    return responce.json()

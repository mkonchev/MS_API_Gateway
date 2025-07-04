import httpx
from fastapi import FastAPI

app = FastAPI()

ORDER_SERVICE = "http://order"
CATALOG_SERVICE = "http://catalog"
USER_SERVICE = "http://users"


@app.get("/")
def reed_root():
    return {"message": "Gateway service"}


@app.get("/catalog")
async def get_products():
    async with httpx.AsyncClient() as client:
        responce = await client.get(f"{CATALOG_SERVICE}/catalog/")
    return responce.json()


@app.post("/order/create")
async def craete_order(product_id: int, quantity: int):
    async with httpx.AsyncClient() as client:
        responce = await client.post(
            f"{ORDER_SERVICE}/orders/",
            json={"product_id": product_id, "quantity": quantity}
        )
    return responce.json()


@app.post("/users/register")
async def register(
                email: str,
                username: str,
                password: str,
):
    async with httpx.AsyncClient(follow_redirects=True) as client:
        responce = await client.post(
            f"{USER_SERVICE}/users/register/",
            json={"email": email,
                  "username": username,
                  "password": password,
                  "active": True}
        )
    return responce.json()

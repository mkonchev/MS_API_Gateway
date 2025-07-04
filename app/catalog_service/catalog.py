import httpx
from fastapi import APIRouter


router = APIRouter()


CATALOG_SERVICE = "http://catalog"


@router.get("/catalog")
async def get_products():
    async with httpx.AsyncClient() as client:
        responce = await client.get(f"{CATALOG_SERVICE}/catalog/")
    return responce.json()

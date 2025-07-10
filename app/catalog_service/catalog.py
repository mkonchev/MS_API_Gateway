import httpx
import os
from dotenv import load_dotenv
from fastapi import APIRouter


router = APIRouter(prefix="/catalog", tags=["Catalog"])


load_dotenv()
CATALOG_SERVICE = os.getenv("CATALOG_SERVICE")


@router.get("/")
async def get_products():
    async with httpx.AsyncClient() as client:
        responce = await client.get(f"{CATALOG_SERVICE}/catalog/")
    return responce.json()

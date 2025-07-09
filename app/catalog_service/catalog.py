import httpx
import os
from dotenv import load_dotenv
from fastapi import APIRouter


router = APIRouter()


load_dotenv()
CATALOG_SERVICE = os.getenv("CATALOG_SERVICE")


@router.get("/catalog")
async def get_products():
    async with httpx.AsyncClient() as client:
        responce = await client.get(f"{CATALOG_SERVICE}/catalog/")
    return responce.json()

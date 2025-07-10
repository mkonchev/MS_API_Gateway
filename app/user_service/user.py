import httpx
import os
from dotenv import load_dotenv
from fastapi import APIRouter


router = APIRouter(prefix="/users", tags=["Users"])


load_dotenv()
USER_SERVICE = os.getenv("USER_SERVICE")


@router.post("/register")
async def register(
    email: str,
    username: str,
    password: str,
):
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.post(
            f"{USER_SERVICE}/users/register/",
            json={
                "email": email,
                "username": username,
                "password": password,
                "active": True
            }
        )
    return response.json()


@router.post("/users/login")
async def login(
    email: str,
    password: str
):
    async with httpx.AsyncClient(follow_redirects=True) as client:
        responce = await client.post(
            f"{USER_SERVICE}/users/login/",
            json={"email": email,
                  "password": password
                  }
        )
    return responce.json()

import httpx
from fastapi import APIRouter


router = APIRouter()


USER_SERVICE = "http://users"


@router.post("/users/register")
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

from fastapi import FastAPI
from app.catalog_service.catalog import router as catalog_router
from app.user_service.user import router as user_router
from app.order_service.order import router as order_router

app = FastAPI()

app.include_router(catalog_router)
app.include_router(user_router)
app.include_router(order_router)


@app.get("/")
def reed_root():
    return {"message": "Gateway service"}

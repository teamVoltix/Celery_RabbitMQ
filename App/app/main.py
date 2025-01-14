from fastapi import FastAPI
from app.api.v1.notifications import router as notifications_router

app = FastAPI()

app.include_router(notifications_router, prefix="/api/v1")
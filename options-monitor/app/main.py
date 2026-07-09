from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="VoIP OPTIONS Monitor",
    version="1.0.0"
)

app.include_router(router)

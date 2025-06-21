from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.api import api_router
from app.core.database import create_tables
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield # desplegar tablas ya existentes

app = FastAPI(
    title="Tecnisis Backend",
    description="Api para el proyecto Tecnisis",
    version="1.0.0",
    docs_url="/documentation", 
    lifespan=lifespan
)

app.include_router(api_router, prefix="/tecnisis")

@app.get("/")
async def root():
    return {"message": "Tecnisi Backend API"}
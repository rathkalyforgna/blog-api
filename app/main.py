from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from fastapi import FastAPI
from .database.db import engine
from .database.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    print("Starting up")
    SQLModel.metadata.create_all(engine)
    yield
    # shutdown or cleanup
    print("Shutting down")
    
app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION,lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello world!"}

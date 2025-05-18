from fastapi import FastAPI
from app import models
from app.database import engine
from app.routes import router

app = FastAPI()

# Create tables in the database
models.Base.metadata.create_all(bind=engine)

# Include the API routes

app = FastAPI()
app.include_router(router)


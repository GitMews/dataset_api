from fastapi import FastAPI
from app.endpoints import router

# Create app
app = FastAPI()

# Add endpoints
app.include_router(router)
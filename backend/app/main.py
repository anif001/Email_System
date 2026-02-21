from fastapi import FastAPI
from app.database import engine
from app import models

# Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Email Intelligence System",
    version="1.0.0"
)

# Simple health check
@app.get("/api/v1/health")
def health_check():
    return {"status": "running"}
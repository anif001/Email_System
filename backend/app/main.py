from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import email


# Create DB tables
models.Base.metadata.create_all(bind=engine)




app = FastAPI(
    title="Email Intelligence System",
    version="1.0.0"
)
# Include API routes
app.include_router(email.router)


# Simple health check
@app.get("/api/v1/health")
def health_check():
    return {"status": "running"}
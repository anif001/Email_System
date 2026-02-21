from fastapi import FastAPI
from app.database import engine    #database.py
from app import models            # models.py
from app.routes import email

# database tables....
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Email Intelligence System",
    version="1.0.0"
)
app.include_router(email.router)

# simple helath checking....
@app.get("/api/v1/health")
def health_check():
        return {"status": "running successfully"}


    # try:
    #     db = SessionLocal()
    #     db.execute("SELECT 1")
    #     return {"status": "healthy"}
    # except:
    #     return {"status": "unhealthy"}


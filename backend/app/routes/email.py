from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas
from app.services import email_service

router = APIRouter(prefix="/api/v1/emails", tags=["Emails"])

@router.post("/", response_model=schemas.EmailResponse)
def create_email(email: schemas.EmailCreate, db: Session = Depends(get_db)):
    return email_service.create_email(db, email)

@router.get("/", response_model=list[schemas.EmailResponse])
def get_emails(db: Session = Depends(get_db)):
    return email_service.get_all_emails(db)
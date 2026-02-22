from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas
from app.services import email_service
from app.services.alert_service import process_pending_alerts
from app.integrations.gmail_fetcher import fetch_unread_emails
router = APIRouter( tags=["Emails"])

@router.post("/emails", response_model=schemas.EmailResponse)
def create_email(email: schemas.EmailCreate, db: Session = Depends(get_db)):
    return email_service.create_email(db, email)

@router.get("/emails", response_model=list[schemas.EmailResponse])
def get_emails(db: Session = Depends(get_db)):
    return email_service.get_all_emails(db)
@router.post("/emails/process-alerts")
def trigger_alerts(db: Session = Depends(get_db)):
    emails = process_pending_alerts(db)
    return {"processed": len(emails)}
from app.integrations.gmail_fetcher import fetch_unread_emails

@router.get("/fetch-gmail")
def fetch_gmail():
    emails = fetch_unread_emails()
    return emails
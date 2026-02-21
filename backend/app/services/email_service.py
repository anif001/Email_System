from sqlalchemy.orm import Session
from app import models

def create_email(db: Session, email_data):
    db_email = models.Email(**email_data.dict())
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return db_email

def get_all_emails(db: Session):
    return db.query(models.Email).all()
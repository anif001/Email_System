import uuid
from sqlalchemy.orm import Session
from datetime import datetime

from app import models
from app.utils.parser import detect_email_attributes


def create_email(db: Session, email_data):

    # 1️⃣ Always generate message_id internally
    generated_id = str(uuid.uuid4())

    # 2️⃣ Smart classification
    category, priority = detect_email_attributes(
        email_data.subject,
        email_data.body
    )

    # Make priority lowercase for consistency
    priority = priority.lower()

    # 3️⃣ Create email object
    db_email = models.Email(
        message_id=generated_id,
        sender=email_data.sender,
        subject=email_data.subject,
        body=email_data.body,
        category=category.lower(),
        priority=priority,
        status="PROCESSED",
        received_at=datetime.utcnow(),
        processed_at=datetime.utcnow(),
        alert_attempts=0,
        source="manual"
    )

    db.add(db_email)
    db.commit()
    db.refresh(db_email)

    return db_email


def get_all_emails(db: Session):
    return db.query(models.Email).all()


def get_high_priority_emails(db: Session):
    return db.query(models.Email).filter(
        models.Email.priority == "high"
    ).all()


def get_emails_by_category(db: Session, category: str):
    return db.query(models.Email).filter(
        models.Email.category == category.lower()
    ).all()


def get_pending_alerts(db: Session):
    return db.query(models.Email).filter(
        models.Email.is_alert_sent == False,
        models.Email.priority == "high"
    ).all()
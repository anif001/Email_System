from sqlalchemy.orm import Session
from datetime import datetime
from app import models


def send_alert(email: models.Email):
    print(f"ALERT SENT FOR: {email.subject}")
    return True


def process_pending_alerts(db: Session):

    high_priority_emails = db.query(models.Email).filter(
        models.Email.priority == "high",
        models.Email.is_alert_sent == False
    ).all()

    for email in high_priority_emails:
        try:
            success = send_alert(email)

            if success:
                email.is_alert_sent = True
                email.status = "alert_sent"
                email.processed_at = datetime.utcnow()

            db.commit()

        except Exception as e:
            email.alert_attempts += 1
            email.status = "failed"
            email.error_message = str(e)
            db.commit()

    return high_priority_emails
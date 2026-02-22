from sqlalchemy.orm import Session
from datetime import datetime
from app import models
from app.integrations.telegram_service import send_telegram_message


def send_alert(email: models.Email):
    message = f"""ALERT: High priority email received 
    From: {email.sender}
    Subject: {email.subject}
    Body: {email.body}
    Received At: {email.received_at}
    category: {email.category}
    """
    success = send_telegram_message(message)
    return success



def process_pending_alerts(db: Session):

    high_priority_emails = db.query(models.Email).filter(
        models.Email.priority == "high",
        models.Email.status == "PROCESSED",
        # models.Email.is_alert_sent == False
    ).all()

    for email in high_priority_emails:
        try:
            success = send_alert(email)

            if success:
                email.status = "ALERT_SENT"
                email.processed_at = datetime.utcnow()
                db.add(email)
                db.commit()
                db.refresh(email)


        except Exception as e:
            email.alert_attempts += 1
        

            if email.alert_attempts >= 3:
                email.status = "FAILED"
                email.error_message = str(e)    
            else:
                email.status = "RETRYING"
    return high_priority_emails
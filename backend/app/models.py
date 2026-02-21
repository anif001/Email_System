from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from datetime import datetime
from app.database import Base

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(String, unique=True, index=True, nullable=False)
    sender = Column(String, index=True)
    subject = Column(String)
    body = Column(Text)
    category = Column(String, index=True)
    priority = Column(String)
    received_at = Column(DateTime)
    processed_at = Column(DateTime)
    is_alert_sent = Column(Boolean, default=False)
    alert_attempts = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

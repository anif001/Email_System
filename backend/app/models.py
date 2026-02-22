from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from datetime import datetime
from app.database import Base


class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)

    # Unique email identifier (prevents duplicates)
    message_id = Column(String, unique=True, index=True, nullable=False)

    # Email content
    sender = Column(String, index=True)
    subject = Column(String)
    body = Column(Text)

    # Smart classification fields
    category = Column(String, index=True)
    priority = Column(String)

    # Processing state
    status = Column(String, default="RECEIVED")

    # Timestamps
    received_at = Column(DateTime)
    processed_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

    #not required as we can infer from status, but keeping for clarity
    # is_alert_sent = Column(Boolean, default=False)

    # Alert tracking
    status = Column(String, default="RECEIVED")
    alert_attempts = Column(Integer, default=0)
    error_message = Column(Text, nullable=True)

    # Future extensibility
    source = Column(String, default="manual")
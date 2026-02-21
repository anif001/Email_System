from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EmailCreate(BaseModel):
    message_id: str
    sender: str
    subject: str
    body: str
    category: Optional[str] = None
    priority: Optional[str] = None

class EmailResponse(BaseModel):
    id: int
    message_id: str
    sender: str
    subject: str
    body: str
    category: Optional[str]
    priority: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
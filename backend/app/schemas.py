from pydantic import BaseModel, EmailStr


class EmailCreate(BaseModel):
    sender: EmailStr
    subject: str
    body: str


class EmailResponse(BaseModel):
    message_id: str
    sender: EmailStr
    subject: str
    body: str
    category: str
    priority: str
    status: str

    class Config:
        from_attributes = True
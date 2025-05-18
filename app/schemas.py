from pydantic import BaseModel


class NotificationCreate(BaseModel):
    user_id: int
    type: str  # "email", "sms", or "inapp"
    message: str


class NotificationOut(NotificationCreate):
    id: int
    delivered: bool

    class Config:
        orm_mode = True


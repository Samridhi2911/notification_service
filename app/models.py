from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    type = Column(String)  # "email", "sms", or "inapp"
    message = Column(String)
    delivered = Column(Boolean, default=False)


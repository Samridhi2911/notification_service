

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /notifications - Save to DB with delivered=False
@router.post("/notifications", response_model=schemas.NotificationOut)
def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(get_db)):
    new_notification = models.Notification(
        user_id=notification.user_id,
        type=notification.type,
        message=notification.message,
        delivered=False  # Worker will update this
    )
    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)
    return new_notification

# GET /users/{id}/notifications - Get all notifications for a user
@router.get("/users/{user_id}/notifications", response_model=list[schemas.NotificationOut])
def get_user_notifications(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Notification).filter(models.Notification.user_id == user_id).all()

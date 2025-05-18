

import time
import random
from app.database import SessionLocal
from app import models

def send_notification(notification, max_retries=3):
    for attempt in range(max_retries):
        print(f"📨 Attempt {attempt+1}: Sending {notification['type']} to user {notification['user_id']}")
        if random.random() > 0.3:
            print("✅ Sent successfully!")
            return True
        print("❌ Failed to send, retrying...")
        time.sleep(1)
    print("💥 Giving up after 3 attempts.")
    return False

def process_pending_notifications():
    db = SessionLocal()
    while True:
        # Get notifications that haven't been sent yet
        pending = db.query(models.Notification).filter_by(delivered=False).all()

        for notification in pending:
            success = send_notification({
                "user_id": notification.user_id,
                "type": notification.type,
                "message": notification.message
            })

            # Update delivered status
            notification.delivered = success
            db.commit()

            print(f"🗂️ Processed notification {notification.id}, success={success}")

        time.sleep(2)  # Check every 2 seconds

if __name__ == "__main__":
    print("🤖 Worker started. Listening for new notifications...")
    process_pending_notifications()



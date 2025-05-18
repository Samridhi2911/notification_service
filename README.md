# 📨 Notification Service (FastAPI + Background Worker + Retries)

This is a simple notification service built using **FastAPI**, with a **background worker** that processes pending notifications from the database using **retry logic**.

---

## ✨ Features

- ✅ Send notifications to users
- ✅ Get all notifications by user ID
- ✅ Supports notification types: `email`, `sms`, `inapp`
- ✅ Background worker retries failed notifications up to 3 times
- ✅ Stores delivery status in SQLite database
- ✅ Auto-generated Swagger UI documentation at `/docs`

---

## 📁 Project Structure

notification_service/
├── app/
│ ├── main.py
│ ├── routes.py                                                  
│ ├── models.py                                                
│ ├── database.py                                         
│ └── schemas.py
├── workers/
│ └── notification_worker.py 
├── README.md 
├── requirements.txt 
├── .gitignore 


---

## 🚀 Getting Started

### 1️⃣ Clone the Repo

2️⃣ Create & Activate Virtual Environment

python -m venv venv
venv\Scripts\activate       # On Windows
# OR
source venv/bin/activate    # On Mac/Linux


3️⃣ Install Requirements

pip install -r requirements.txt


🧪 How to Run the Project

▶️ Terminal 1: Start FastAPI App

uvicorn app.main:app --reload

Access API docs at:
http://127.0.0.1:8000/docs


▶️ Terminal 2: Start the Worker

python -m workers.notification_worker



The worker:

1.Picks up all undelivered notifications from the database

2.Simulates sending

3.Retries up to 3 times if sending fails

4.Marks them as delivered: true in DB if successful

📬 API Documentation

📌 POST /notifications

Create a new notification.

✅ Request Body
    
      {
       "user_id": 1,
       "type": "email",
     "message": "Hello from the notification service!"
      }

✅ Response

    {
     "id": 1,
    "user_id": 1,
    "type": "email",
    "message": "Hello from the notification service!",
    "delivered": false
   }


📌 GET /users/{user_id}/notifications

Fetch all notifications for a user.

✅ Example

   GET /users/1/notifications

✅ Response

  [
    {
      "id": 1,
     "user_id": 1,
     "type": "email",
     "message": "Hello!",
     "delivered": true
    },

    {
     "id": 2,
     "user_id": 1,
     "type": "sms",
     "message": "Reminder",
     "delivered": false
    }
 ]

📌 Assumptions Made

 -No real message delivery (email/SMS is simulated with print()).

 -No real user authentication.

 -SQLite used for local development (no PostgreSQL/Redis).

 -Delivery failures are randomly simulated (30% fail chance).


🧠 Bonus Features Implemented

 ✅ Background worker

 ✅ Retry mechanism (3 attempts)

 ✅ Delivery status tracking

 ✅ Clean project structure

📌 Requirements

 fastapi
 uvicorn
 sqlalchemy
 pydantic

from pymongo import MongoClient
from datetime import datetime, timezone

MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)
db = client.notifications_db

mock_notifications = [
    {
        "user_id": "101",
        "type": "email",
        "message": "Welcome to our service!",
        "status": "sent",
        "timestamp": datetime.now(timezone.utc)
    },
    {
        "user_id": "101",
        "type": "sms",
        "message": "Your verification code is 123456.",
        "status": "sent",
        "timestamp": datetime.now(timezone.utc)
    },
    {
        "user_id": "102",
        "type": "in-app",
        "message": "You have a new friend request.",
        "status": "sent",
        "timestamp": datetime.now(timezone.utc)
    }
]

result = db.notifications.insert_many(mock_notifications)
print(f"Inserted {len(result.inserted_ids)} mock notifications.")

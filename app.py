from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import datetime

app = Flask(__name__)

MONGO_URI = "mongodb://localhost:27017"  
client = MongoClient(MONGO_URI)
db = client.notifications_db

def serialize_notification(notif):
    notif["_id"] = str(notif["_id"])
    notif["timestamp"] = notif["timestamp"].isoformat()
    return notif


@app.route('/')
def index():
    return jsonify({
        "message": " Notification Service is running.",
        "endpoints": {
            "Send Notification": "POST /notifications",
            "Get User Notifications": "GET /users/<user_id>/notifications"
        }
    })


@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.get_json()
    required_fields = {"user_id", "type", "message"}

    if not data or not required_fields.issubset(data):
        return jsonify({"error": "Missing required fields"}), 400

    notif = {
        "user_id": data["user_id"],
        "type": data["type"],  
        "message": data["message"],
        "status": "sent",
        "timestamp": datetime.datetime.utcnow()
    }

    result = db.notifications.insert_one(notif)
    return jsonify({"message": "Notification sent", "id": str(result.inserted_id)}), 201

@app.route('/users/<user_id>/notifications', methods=['GET'])
def get_user_notifications(user_id):
    notifs = db.notifications.find({"user_id": user_id})
    return jsonify([serialize_notification(n) for n in notifs]), 200

if __name__ == '__main__':
    app.run(debug=True)
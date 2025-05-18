# Notification Service

A simple RESTful API to send and retrieve notifications (Email, SMS, In-App) for users.

## Overview

This Notification Service provides a centralized system for managing and delivering various types of notifications to users. The service handles the storage, retrieval, and delivery of notifications across multiple channels including Email, SMS, and In-App notifications.

## Features

- Store notifications in MongoDB
- Send notifications via multiple channels
- Retrieve notification history for users
- RESTful API interface for easy integration

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: MongoDB
- **Object ID Handling**: BSON
- **Date/Time Handling**: Python datetime

## Prerequisites

- Python 3.6+
- MongoDB running on localhost:27017 (or configured connection string)
- Pip for package installation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/barmansagarika/notification-service.git
cd notification-service
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Make sure MongoDB is running:
```bash
# Start MongoDB locally
mongod --dbpath /path/to/data/db
```

## Configuration

The service connects to MongoDB using the connection string defined in `app.py`. By default, it uses:
```
mongodb://localhost:27017
```

To modify the connection settings, update the `MONGO_URI` variable in `app.py`.

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. The API will be available at `http://localhost:5000`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Basic health check and API information |
| `/notifications` | POST | Create and send a new notification |
| `/users/<user_id>/notifications` | GET | Retrieve all notifications for a specific user |


## Data Structure

Notifications are stored with the following structure:
- `_id`: Unique identifier (MongoDB ObjectId)
- `timestamp`: Time when the notification was created


## Development

The project structure is organized as follows:
- `app.py`: Main application entry point and API routes
- `mock_data.py`: Sample data for testing
- `requirements.txt`: Project dependencies


## Contact

Sagarika Barman - [GitHub Profile](https://github.com/barmansagarika)

Project Link: [https://github.com/barmansagarika/notification-service](https://github.com/barmansagarika/notification-service)

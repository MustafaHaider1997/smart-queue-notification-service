# 📣 Smart Queue - Notification Service

The **Notification Service** is a microservice within the **Smart Queue Management System** responsible for listening to real-time queue updates and sending **email alerts** to patients using **Azure Communication Services (ACS Email)**.

---

## 🚀 Features

* 📨 Subscribes to Redis `queue_updates` for real-time events
* 📧 Sends transactional email alerts (new appointments, updates, etc.)
* 🔐 Uses Azure Communication Services for authenticated email delivery
* 🔄 Works seamlessly with Appointment and Queue services
* 🐳 Dockerized and orchestratable with Docker Compose

---

## 🛠️ Tech Stack

| Component      | Technology                    |
| -------------- | ----------------------------- |
| **Language**   | Python 3.12                   |
| **Framework**  | Flask (minimal use)           |
| **Messaging**  | Redis (Azure Cache for Redis) |
| **Email**      | Azure Communication Services  |
| **Deployment** | Docker, Docker Compose        |

---

## 📁 Project Structure

```
smart-queue-notification-service/
├── app.py                  # Optional Flask app (not required)
├── redis_listener.py       # Main Redis subscriber script
├── notification.py         # Email sending logic using Azure SDK
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker setup
├── .env                    # Configuration variables
└── venv/                   # Local virtualenv (excluded in container)
```

---

## 🔐 Environment Variables (.env)

You must configure the following variables in `.env`:

```env
# Redis
REDIS_HOST=smartqueueredis.redis.cache.windows.net
REDIS_PORT=6380
REDIS_PASSWORD=your_redis_password
REDIS_USE_SSL=True

# Azure Communication Email
AZURE_COMMUNICATION_CONNECTION_STRING=endpoint=https://<your-endpoint>.communication.azure.com/;accesskey=your_key
AZURE_SENDER_EMAIL=donotreply@<your-domain>.azurecomm.net
AZURE_TO_EMAIL=recipient@example.com  # For testing
```

---

## 🧪 Sample Queue Message

```json
{
  "event": "appointment_created",
  "data": {
    "appointmentId": "abcd-1234",
    "patientName": "John Doe",
    "time": "2025-05-10T10:00:00Z"
  }
}
```

---

## ▶️ Running the Service

### Local

```bash
pip install -r requirements.txt
python redis_listener.py
```

You will see:

```
📡 Starting Redis Listener...
✅ Subscribed to 'queue_updates' channel.
Received: New appointment created with ID: ...
📧 Email sent successfully!
```

---

## 🐳 Docker Instructions

### Build

```bash
docker build -t smart-queue-notification-service .
```

### Run

```bash
docker run --env-file .env smart-queue-notification-service
```

Or via Docker Compose:

```yaml
notification-service:
  build: ./smart-queue-notification-service
  command: python redis_listener.py
  env_file:
    - ./smart-queue-notification-service/.env
  depends_on:
    - queue-service
    - appointment-service
```

---

## 📬 Email Sending Logic

Implemented using the [Azure Communication Services Python SDK](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/send-email?pivots=programming-language-python).

```python
from azure.communication.email import EmailClient
client = EmailClient(connection_string)
response = client.begin_send(message)
```

---

## 🔄 Integration Flow

1. **Appointment Service** publishes a queue update via Redis.
2. **Queue Service** relays this message.
3. **Notification Service** listens and sends an email via ACS.
4. Result: Patient gets notified in real-time.

---

## 📄 License

This project is licensed under the MIT License.

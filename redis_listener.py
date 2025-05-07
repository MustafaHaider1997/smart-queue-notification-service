import redis
import os
from dotenv import load_dotenv
from notification import send_email

load_dotenv()

def listen_to_redis():
    print("📡 Starting Redis Listener...")

    try:
        redis_url = f"rediss://:{os.getenv('REDIS_PASSWORD')}@{os.getenv('REDIS_HOST')}:{os.getenv('REDIS_PORT')}"
        r = redis.Redis.from_url(redis_url)
        pubsub = r.pubsub()
        pubsub.subscribe("queue_updates")

        print("✅ Subscribed to 'queue_updates' channel.")

        for message in pubsub.listen():
            if message["type"] == "message":
                payload = message["data"].decode()
                print(f"🔔 Received: {payload}")
                send_email("Queue Update", payload)

    except Exception as e:
        print(f"❌ Redis listener failed: {e}")

if __name__ == "__main__":
    listen_to_redis()
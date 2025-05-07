import os
from dotenv import load_dotenv
from azure.communication.email import EmailClient

load_dotenv()

def send_email(subject: str, body: str):
    connection_string = os.getenv("AZURE_COMMUNICATION_CONNECTION_STRING")
    sender = os.getenv("AZURE_SENDER_EMAIL")
    recipient = os.getenv("AZURE_TO_EMAIL")

    client = EmailClient.from_connection_string(connection_string)

    message = {
        "senderAddress": sender,
        "recipients": {
            "to": [{"address": recipient}]
        },
        "content": {
            "subject": subject,
            "plainText": body
        }
    }

    try:
        poller = client.begin_send(message)
        result = poller.result()  # Waits for completion
        print(f"✅ Email sent! Response:\n{result}")
    except Exception as e:
        print(f"❌ Email send failed: {e}")
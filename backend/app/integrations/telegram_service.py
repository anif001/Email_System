import requests
from app.config import settings


def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=payload)

    return response.status_code == 200
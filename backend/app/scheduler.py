from apscheduler.schedulers.background import BackgroundScheduler
from app.integrations.gmail_fetcher import fetch_unread_emails
from app.integrations.telegram_service import send_telegram_message

def gmail_job():
    emails = fetch_unread_emails(limit=5)

    for email in emails:
        if is_valid_email(email):
            send_telegram_message(format_message(email))


def is_valid_email(email):
    text = (email["subject"] + " " + email["body"]).lower()

    unwanted_keywords = [
        "sale",
        "discount",
        "offer",
        "unsubscribe",
        "promotion",
        "newsletter"
    ]

    for word in unwanted_keywords:
        if word in text:
            return False

    return True


def format_message(email):
    return f"""
📩 NEW EMAIL

From: {email['sender']}
Subject: {email['subject']}
Date: {email['date']}

Preview:
{email['body'][:300]}
"""


scheduler = BackgroundScheduler()
scheduler.add_job(gmail_job, "interval", minutes=1)
scheduler.start()
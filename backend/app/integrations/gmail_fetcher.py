import imaplib
import email
from email.header import decode_header
from app.config import settings


def fetch_unread_emails(limit: int = 10):
    mail = imaplib.IMAP4_SSL(settings.IMAP_SERVER, settings.IMAP_PORT)
    mail.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)
    mail.select("inbox")

    # Get unread emails
    status, messages = mail.search(None, "UNSEEN")

    if status != "OK":
        mail.logout()
        return []

    email_ids = messages[0].split()

    # Take only latest N emails 
    email_ids = email_ids[-limit:]
    # reverse to get newest first
    email_ids.reverse()

    results = []

    for num in email_ids:
        status, msg_data = mail.fetch(num, "(RFC822)")
        if status != "OK":
            continue

        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                # Decode subject safely
                subject, encoding = decode_header(msg.get("Subject"))[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8", errors="ignore")

                sender = msg.get("From")
                date = msg.get("Date")

                body = ""

                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))

                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            payload = part.get_payload(decode=True)
                            charset = part.get_content_charset()

                            if payload:
                                body = payload.decode(charset or "utf-8", errors="ignore")
                            break
                else:
                    payload = msg.get_payload(decode=True)
                    charset = msg.get_content_charset()

                    if payload:
                        body = payload.decode(charset or "utf-8", errors="ignore")

                results.append({
                    "sender": sender,
                    "subject": subject,
                    "body": body[:1000],  # limit body size
                    "date": date
                })

    mail.logout()
    return results
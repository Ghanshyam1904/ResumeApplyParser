import smtplib
from email.mime.text import MIMEText
from config import EMAIL, EMAIL_PASSWORD

def send_email(report):
    msg = MIMEText(report)
    msg["Subject"] = "AutoApply AI Report"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, EMAIL_PASSWORD)
        server.send_message(msg)
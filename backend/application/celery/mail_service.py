import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "localhost"
SMTP_PORT = 1025
SENDER_EMAIL = "project@madypro.in"
SENDER_PASSWORD = ""

def send_email(to, subject, content):
    message = MIMEMultipart()
    message['To'] = to
    message['Subject'] = subject
    message['From'] = SENDER_EMAIL

    message.attach(MIMEText(content, 'plain'))

    with smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT) as client:
        client.send_message(message)
        client.quit()

# send_email('dev@gmail.in', 'Welcome Onboard', 'Hii Dev, this is Aron from Madypro.')
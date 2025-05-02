import os
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv

# Load environment variables from .env file (if exists)
load_dotenv()

# Sender information
sender_name = "Debt Collector"
sender_email = os.environ.get("EMAIL_ADDRESS")
sender_password = os.environ.get("EMAIL_PASSWORD")
receiver_email = 'anotheremail@gmail.com'

# Email content
subject = 'Outstanding Debt'
body = """
You owe $15,000.

Please pay using the following link:
https://paypal.me/branxz07

Regards,
Your Name.
"""

# Creating an email message
email_message = EmailMessage()
email_message['From'] = f'{sender_name} <{sender_email}>'
email_message['To'] = receiver_email
email_message['Subject'] = subject
email_message.set_content(body)

# SSL context
context = ssl.create_default_context()

# Send email once (example)
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender_email, sender_password)
    smtp.sendmail(sender_email, receiver_email, email_message.as_string())


# Function to send an email with parameters (for testing/reuse)
def send_email(subject, body, recipient, sender, password, smtp_server, smtp_port):
    """
    Sends an email using SMTP.
    
    :return: True on success, False on failure.
    """
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['To'] = recipient
        msg['From'] = sender

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(
            smtp_server,
            smtp_port
        ) as server:

            server.login(sender, password)
            server.send_message(msg)

        return True
    except Exception as e:
        print(
            f"Error sending email: {e}"
        )
        return False

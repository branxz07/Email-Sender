import os
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv

# Load environment variables from .env file (if exists)
load_dotenv()

# Sender information
sdr_name = "Debt Collector"
sdr_email = os.environ.get("EMAIL_ADDRESS")
sdr_password = os.environ.get("EMAIL_PASSWORD")
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
email_message['From'] = f'{sdr_name} <{sdr_email}>'
email_message['To'] = receiver_email
email_message['Subject'] = subject
email_message.set_content(body)

# Send email once (example)
with smtplib.SMTP_SSL(
    'smtp.gmail.com',
    465
) as smtp:
    smtp.login(sdr_email, sdr_password)
    smtp.sendmail(
        sdr_email,
        receiver_email,
        email_message.as_string()
    )


# Function to send an email with parameters (for testing/reuse)
def send_email(subject, body, recipient, sdr, password, smtp_server, smtp_port):
    """
    Sends an email using SMTP.
    
    :return: True on success, False on failure.
    """
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['To'] = recipient
        msg['From'] = sdr

        # Removed unused context variable
        # context = ssl.create_default_context()

        with smtplib.SMTP_SSL(
            smtp_server,
            smtp_port
        ) as server:

            server.login(sdr, password)
            server.send_message(msg)

        return True
    except Exception as e:
        print(
            f"Error sending email: {e}"
        )
        return False

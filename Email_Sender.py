import os
from email.message import EmailMessage
import ssl
import smtplib

# Example Documentation Format:
"""[Summary]

:param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
:type [ParamName]: [ParamType](, optional)
...
:raises [ErrorType]: [ErrorDescription]
...
:return: [ReturnDescription]
:rtype: [ReturnType]
"""

# Sender information
sender_name = "Debt Collector"
sender_email = 'youremail@gmail.com'  # Replace with your actual email
sender_password = "xxxx xxxx xxxx xxxx"  # Use environment variable for security
receiver_email = 'anotheremail@gmail.com'  # Receiver email

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

# SSL context for secure email sending
context = ssl.create_default_context()

# Sending the email using SMTP SSL
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender_email, sender_password)
    smtp.sendmail(sender_email, receiver_email, email_message.as_string())

# Function to send an email with configurable parameters
def send_email(subject, body, recipient, sender, password, smtp_server, smtp_port):
    """
    Sends an email using SMTP.
    
    :param subject: Email subject
    :type subject: str
    :param body: Email body content
    :type body: str
    :param recipient: Receiver's email address
    :type recipient: str
    :param sender: Sender's email address
    :type sender: str
    :param password: Sender's email password (Use environment variables for security)
    :type password: str
    :param smtp_server: SMTP server address
    :type smtp_server: str
    :param smtp_port: SMTP server port
    :type smtp_port: int
    :return: None
    """
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['To'] = recipient
    msg['From'] = sender
    
    # Secure connection context
    context = ssl.create_default_context()
    
    # Sending email
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls(context=context)
        smtp.login(sender, password)
        smtp.send_message(msg)

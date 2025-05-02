import os
import sys
from unittest.mock import patch, MagicMock

# Add src to path before any other imports to allow import of email_sdr module
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../src'
        )
    )
)

from email_sender import send_email


def test_send_email_success(monkeypatch):
    monkeypatch.setenv("EMAIL_ADDRESS", "testsdr@example.com")
    monkeypatch.setenv("EMAIL_PASSWORD", "fakepassword")

    # Patch the correct SMTP class used in the function
    with patch("smtplib.SMTP_SSL") as mock_smtp:
        mock_instance = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_instance

        result = send_email(
            subject="Test Subject",
            body="This is a test email.",
            recipient="receiver@example.com",
            sdr="testsdr@example.com",
            password="fakepassword",
            smtp_server="smtp.gmail.com",
            smtp_port=465,
        )

        assert result is True
        mock_instance.login.assert_called_once_with("testsdr@example.com", "fakepassword")
        mock_instance.send_message.assert_called_once()

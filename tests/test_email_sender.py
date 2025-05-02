import os
import pytest
from Email_Sender import send_email
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


def test_send_email_success(monkeypatch):
    monkeypatch.setenv("EMAIL_ADDRESS", "testsender@example.com")
    monkeypatch.setenv("EMAIL_PASSWORD", "fakepassword")

    # Mock SMTP object
    with patch("smtplib.SMTP") as mock_smtp:
        mock_instance = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_instance

        result = send_email(
            subject="Test Subject",
            body="This is a test email.",
            recipient="receiver@example.com"
        )

        assert result is True
        mock_instance.login.assert_called_once_with("testsender@example.com", "fakepassword")
        mock_instance.send_message.assert_called_once()

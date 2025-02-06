# Email Sender Script

This Python script sends emails using SMTP with SSL security. It allows for sending customized email messages with configurable parameters.

## Features

- Sends emails securely using SSL.
- Supports customizable sender and receiver details.
- Allows dynamic email subject and body.
- Uses an environment variable for security (recommended for email credentials).
- Includes a function for reusable email sending.

## Requirements

- Python 3.x
- `smtplib` library (built-in)
- `ssl` library (built-in)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-repo/Email-Sender.git
    cd Email-Sender
    ```
2. **Set up email credentials securely:**
    - Store your email credentials in environment variables to enhance security.
    ```sh
    export EMAIL_SENDER='youremail@gmail.com'
    export EMAIL_PASSWORD='your-secure-app-password'
    ```

## Usage

1. **Modify sender and receiver details:**
    - Update `sender_email` and `receiver_email` in the script.
2. **Run the script:**
    ```sh
    python email_sender.py
    ```
3. **Using the function for dynamic email sending:**
    ```python
    send_email(
        subject="Your Subject",
        body="Your message here",
        recipient="receiver@example.com",
        sender=os.getenv("EMAIL_SENDER"),
        password=os.getenv("EMAIL_PASSWORD"),
        smtp_server='smtp.gmail.com',
        smtp_port=587
    )
    ```

## Notes

- Make sure to enable "Less Secure Apps" in your Gmail settings or use an app password.
- It is highly recommended to store credentials in environment variables instead of hardcoding them in the script.
- This script uses Gmail's SMTP server by default but can be configured for other email providers.

## Contributing

Contributions are welcome! Open an issue or submit a pull request for improvements or bug fixes.

## License

This project is free to use and modify.

## Disclaimer

This script is for educational and informational purposes only. Use it responsibly and comply with email service provider policies.

## Contact

For any questions or suggestions, please open an issue.


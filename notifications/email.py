import os
from dotenv import load_dotenv
import smtplib


def send_email(email_body, server):
    """Logic to send the email to the given email address(s)."""

    # load environment variables from .env
    load_dotenv()

    with smtplib.SMTP(server, port=587) as connection:
        connection.starttls()
        connection.login(os.getenv("FROM_EMAIL"), os.getenv("EMAIL_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("FROM_EMAIL"),
            to_addrs=os.getenv("TO_EMAIL"),
            msg=f"Subject:Websites Down\n\n{email_body}.",
        )

    print("Email has been sent")

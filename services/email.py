import smtplib
from email.message import EmailMessage
from models.email import EmailResponse
from config import get_settings

class EmailService:

    def __init__(self):
        self.settings = get_settings()

    def send(
        self,
        receiver,
        subject,
        message,
    ) -> EmailResponse:
        em = EmailMessage()
        em["From"] = self.settings.EMAIL_SENDER
        em["To"] = receiver
        em["Subject"] = subject
        em.set_content(message)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(self.settings.EMAIL_SENDER, self.settings.SENDER_PASSWORD)
            smtp.sendmail(self.settings.EMAIL_SENDER, receiver, em.as_string())

        return EmailResponse(OK=True)
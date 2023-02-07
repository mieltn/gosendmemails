from fastapi import APIRouter, Depends
from models.email import EmailRequest, EmailResponse
from services.email import EmailService

router = APIRouter(prefix="/api")

@router.post("/send/email")
def send_email(
    body: EmailRequest,
    email_service: EmailService = Depends(),
) -> EmailResponse:
    return email_service.send(
        receiver=body.receiver,
        subject=body.subject,
        message=body.message,
    )

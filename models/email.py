from pydantic import BaseModel


class EmailRequest(BaseModel):
    receiver: str
    subject: str
    message: str


class EmailResponse(BaseModel):
    OK: bool
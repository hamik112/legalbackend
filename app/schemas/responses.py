from pydantic import BaseModel

class CCPAResponse(BaseModel):
	message: str = "Thank you. We've received your CCPA request and will process your request within the next 7 business days. Please check your email for a response."


class ContactResponse(BaseModel):
	message: str = "Thank you for contacting us. We will get back to you soon."

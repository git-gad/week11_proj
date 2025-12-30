from pydantic import BaseModel

class ContactOutput(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    
class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
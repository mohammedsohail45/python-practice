from pydantic import BaseModel, EmailStr

# Request schema for creating personal info
class PersonalInfoCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: str
    address: str

# Response schema for reading personal info
class PersonalInfoOut(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: str
    address: str

    class Config:
        orm_mode = True

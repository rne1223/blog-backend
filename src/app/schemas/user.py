from pydantic import BaseModel, EmailStr
from typing import Optional

# API to DB Schemas
class UserBase(BaseModel):
    first_name: Optional[str]
    surname: Optional[str]
    email: Optional[EmailStr] = None
    is_superuser: bool = False

# Properties to receive via Api on creation
class UserCreate(UserBase):
    email: EmailStr


# Porperties to receive via Api on update
class UserUpdate(UserBase):
    pass

# DB to API Schemas
class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

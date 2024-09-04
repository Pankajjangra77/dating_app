from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserBase(BaseModel):
    name: str
    age: int
    gender: str
    email: EmailStr 
    city: str
    interests: List[str]


class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True


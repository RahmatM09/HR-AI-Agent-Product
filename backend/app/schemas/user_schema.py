from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length = 8)
    company_name: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    company_name: Optional[str] = None
    is_active: bool

    class Config:
        from_attributes = True
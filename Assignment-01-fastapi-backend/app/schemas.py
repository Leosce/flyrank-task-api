from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    age: int | None = Field(default=None, gt=0)


class UserCreate(UserBase):
    """Payload accepted when creating a user."""


class UserUpdate(UserBase):
    """Full replacement payload accepted when updating a user."""


class UserResponse(UserBase):
    id: int

from pydantic import BaseModel, EmailStr


class SignInRequest(BaseModel):
    username: str
    password: str


class SignOutRequest(BaseModel):
    username: str

class CreateUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import EmailStr, SecretStr

from app.models import User
from app.schemas import BaseModel


class CreateUserSchema(BaseModel):
    email: EmailStr
    phone_number: str
    password: SecretStr
    first_name: str
    last_name: str


class LoginSchema(BaseModel):
    phone_number: str
    password: SecretStr


user_schema = pydantic_model_creator(
    User, 
    name='user_schema', 
    exclude = ["password"],
    allow_cycles = False
    )
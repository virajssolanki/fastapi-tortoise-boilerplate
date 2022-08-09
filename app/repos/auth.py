from datetime import datetime, timedelta
from pydantic import UUID4
import uuid
from jose import jwt
from passlib.context import CryptContext
from fastapi import status
from app.core.exception import APIException
from app.core import messages
from app.schemas import *
from app.core.config import get_app_settings

from typing import Optional


settings = get_app_settings()
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_and_update_password(
    plain_password: str, password: str
    ) -> tuple[bool, str]:
    return password_context.verify_and_update(plain_password, password)


def get_password_hash(password: str) -> str:
    return password_context.hash(password)


async def authenticate(credentials: LoginSchema) -> Optional[User]:
    if not credentials.phone_number:
        return None

    user = await User.get_or_none(phone_number=credentials.phone_number)

    if user is None:
        return None

    verified, updated_password_hash = verify_and_update_password(
        credentials.password.get_secret_value(), user.password
    )

    if not verified:
        return None

    if updated_password_hash is not None:
        user.password = updated_password_hash
        await user.save()

    return user



def get_token(data: dict, expires_delta: int):
    to_encode = data.copy()
    to_encode.update({
        "exp": datetime.utcnow() + timedelta(seconds=expires_delta),
        "iss": settings.title
    })
    return jwt.encode(
        to_encode,
        settings.secret_key.get_secret_value(),
        algorithm=settings.token_algorithm
    )


def get_access_token(user_id: UUID4, scopes:list):
    jti = uuid.uuid4()
    claims = {
        "user_id": str(user_id),
        "scopes": scopes
    }
    return {
        "jti": jti,
        "token": get_token(
            claims,
            settings.token_lifetime
        )
    }

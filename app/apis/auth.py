from fastapi import APIRouter

from app.repos import authenticate, get_access_token, create_user
from app.schemas import LoginSchema, CreateUserSchema
from app.models import User

from app.core.response import ResponseInfo, get_response_model
from app.core.config import get_app_settings
from app.core import messages
from app.core.exception import AuthenticationFailed, ConflictException


settings = get_app_settings()


router = APIRouter()


@router.post("/login/")
async def login(credentials: LoginSchema):
    ''''
    authenticate the user
    '''
    user = await authenticate(credentials)
    if not user:
        raise AuthenticationFailed()

    elif user.is_locked:
        raise AuthenticationFailed("User account is locked.")

    access_token = get_access_token(user_id=user.id, scopes=[user.user_type, ])

    res = ResponseInfo(
        {
            "access_token": access_token["token"],
            "token_type": "bearer"
        },
        messages.LOGGED_IN, True, 200
    )

    return res.success_payload()


@router.post("/sign_up/", response_model=get_response_model(CreateUserSchema))
async def user_signup(data: CreateUserSchema):
    '''
    create new user
    by default it will have user type of restaurant-owner
    '''
    if await User.get_or_none(phone_number=data.phone_number) is not None:
        raise ConflictException(detail="User with Phone Number already exist.")

    user = await create_user(data)

    res = ResponseInfo(user, messages.ACCOUNT_CREATED, True, 201)
    return res.success_payload()
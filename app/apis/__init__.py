from fastapi import APIRouter
from app.apis import (auth)
from app.core.tags import Tags
from app.core.config import get_app_settings


settings = get_app_settings()


api_router = APIRouter()

api_router.include_router(auth.router, tags=[Tags.auth])

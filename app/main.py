from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.starlette import register_tortoise
from app.apis import api_router
from app.core.exception import HTTPException, http_exception_handler
from app.core.config import get_app_settings


def get_application() -> FastAPI:
    settings = get_app_settings()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts, allow_credentials=True,
        allow_methods=["*"], allow_headers=["*"],
    )

    application.add_exception_handler(
        HTTPException, http_exception_handler
    )

    application.include_router(api_router, prefix=settings.api_prefix)
    # application.include_router(media_router, prefix=settings.media_url)

    register_tortoise(
        application,
        config=settings.tortoise_config,
        generate_schemas=settings.generate_schemas,
    )
    return application


"""
initialize fastapi app
"""
app = get_application()


"""
initigrate aerich for migrations
"""
aerich_config = get_app_settings().tortoise_config


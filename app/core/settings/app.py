from pathlib import Path
from typing import Any, Dict, List

from pydantic import PostgresDsn, SecretStr

from app.core.settings.base import BaseAppSettings
from tortoise.backends.base.config_generator import generate_config


class AppSettings(BaseAppSettings):
    debug: bool = False
    docs_url: str = "/"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "megrut-apis"
    version: str = "0.0.1"

    #tortoise settings
    modules: dict = {"models": ["app.models", 'aerich.models',] }   
    database_url: PostgresDsn
    generate_schemas: bool = True

    # smtp_server: str
    # mail_sender = 'noreply@example.com'

    max_connection_count: int = 10
    min_connection_count: int = 10

    secret_key: SecretStr

    api_prefix: str = "/api"
    
    base_dir: Path = Path(__file__).resolve().parent.parent.parent.parent

    media_root: str = "media" #used to store files
    media_url: str = "/media" #used to get files or define url

    html_root: str = 'html'

    jwt_token_prefix: str = "Token"
    token_algorithm = 'HS256'
    token_lifetime = 60 * 60 *60

    allowed_hosts: List[str] = ["*"]

    class Config:
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }

    @property
    def tortoise_config(self) -> Dict[str, Any]:
        config = generate_config(self.database_url, self.modules)
        return config

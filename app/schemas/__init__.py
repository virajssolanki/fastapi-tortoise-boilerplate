from tortoise import Tortoise
from app.core.config import get_app_settings

"""
Initialise the relationships between Models. This does not initialise any database connection.
"""
Tortoise.init_models(
    get_app_settings().tortoise_config['apps']['models']['models'], 'models',
    _init_relations=True
    )


from .base import BaseModel
from .user import *

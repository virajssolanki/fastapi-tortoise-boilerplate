from tortoise import fields
from tortoise.validators import *

from app.models.base import BaseModel
from app.core import roles


class User(BaseModel):
    """
    The User model
    """
    phone_number = fields.CharField(max_length=40, unique=True, null=False)
    user_type = fields.CharField(null=False, max_length=255, default=roles.RES_OWNER)
    email = fields.CharField(null=True, max_length=255)
    first_name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=200, null=True)
    is_locked = fields.BooleanField(null=False, default=False)
    last_login = fields.DatetimeField(null=True, auto_now=True)

    class Meta:
        table: str = 'user'
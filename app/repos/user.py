from app.repos import get_password_hash
from app.schemas import CreateUserSchema
from app.models import User


async def create_user(data: CreateUserSchema) -> User:
    user = await User.create(**data.dict(exclude={'password'}),
                        password=get_password_hash(
                                data.password.get_secret_value()
                        )
    )
    
    return user

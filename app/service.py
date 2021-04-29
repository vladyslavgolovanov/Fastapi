from src.core.db import database
from .models import users
from .shemas import UserBase, UserPassword


async def get_users():
    us_list = await database.fetch_all(query=users.select())
    return [dict(result) for result in us_list]


async def create(item: UserBase):
    user = users.insert().values(**item.dict())
    pk = await database.execute(user)
    return {**item.dict(), "id": pk}


async def update_password(pk: int, item: UserPassword):
    user = users.update().where(users.c.id == pk).values(**item.dict())
    return await database.execute(user)


async def delete(pk: int):
    user = users.delete().where(users.c.id == pk)
    return await database.execute(user)



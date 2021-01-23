from typing import List

from fastapi import FastAPI
from app.shemas import UserList, UserBase, UserPassword
from app import service
from core.db import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    return await database.disconnect()


@app.post('/create-user')
async def create_user(item: UserBase):
    return await service.create(item)


@app.put('/update-password')
async def update_password(pk: int, item: UserPassword):
    return await service.update_password(pk, item)


@app.delete('/delete-user')
async def delete_user(pk: int):
    return await service.delete(pk)


@app.get('/get-user-list', response_model=List[UserList])
async def user_list():
    return await service.get_users()

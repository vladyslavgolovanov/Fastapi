from pydantic import BaseModel
from datetime import datetime


class UserPassword(BaseModel):
    password: str


class UserBase(UserPassword):
    username: str
    email: str
    first_name: str
    last_name: str


class UserList(UserBase):
    id: int
    data: datetime

    class Config:
        orm_mode = True



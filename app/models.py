from sqlalchemy import Column, String, Integer, DateTime, sql

from src.core.db import Base


class User(Base):
    __tablename__ = 'users_app'
    id = Column(Integer, primary_key=True, unique=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    data = Column(DateTime(timezone=True), server_default=sql.func.now())


users = User.__table__
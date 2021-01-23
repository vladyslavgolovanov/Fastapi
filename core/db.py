import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()

database = databases.Database(SQLALCHEMY_DATABASE_URL)
Base: DeclarativeMeta = declarative_base()
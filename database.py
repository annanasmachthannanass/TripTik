from sqlalchemy import create_engine

DATABASE_URL = 'mysql://username:password@localhost/dbname'

engine = create_engine(DATABASE_URL, echo=True)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

DATABASE_URL = 'mysql://username:password@localhost/dbname'
engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    fullname = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(100))  # Password hash

Base.metadata.create_all(engine)
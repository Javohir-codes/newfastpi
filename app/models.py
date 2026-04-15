from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)


class Clothes(Base):
    __tablename__ = "clothes"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    price = Column(Integer, nullable=False)
    image_url = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
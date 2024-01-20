from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from app.Models.UserDto import UserDto

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    city = Column(String)
    password = Column(String)
    role = Column(String)
    @classmethod
    def from_dto(cls, user_dto: UserDto):
        return cls(
            name=user_dto.name,
            age=user_dto.age,
            city=user_dto.city,
            role=user_dto.role
        )
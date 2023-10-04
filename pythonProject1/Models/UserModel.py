from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    name: str
    age: int
    city: str
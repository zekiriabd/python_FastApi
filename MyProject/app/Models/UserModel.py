from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    name: str
    age: int
    city: str
    password: str
    role: str


class CredentialModel(BaseModel):
    username: str
    password: str
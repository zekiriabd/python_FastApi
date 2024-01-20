from pydantic import BaseModel

class UserDto(BaseModel):
    id: int
    name: str
    age: int
    city: str
    role: str

    class Config:
        from_attributes = True


class CredentialModel(BaseModel):
    username: str
    password: str

from typing import Optional, Any

from pydantic import BaseModel, constr, EmailStr, Field, PositiveInt


class UserModel(BaseModel):
    id: int
    name: constr(pattern=r'^(ADMIN|USER|BASIC)$')
    age: int
    city: str



from typing import List
from fastapi import FastAPI
from Models.UserModel import UserModel
from Services.UserServices import UserServices

app = FastAPI()
service = UserServices()


@app.get("/users/", tags=["Users"])
async def get_users() -> List[UserModel]:
    return await service.get_users()
@app.get("/users/{user_id}", tags=["Users"])
async def get_user_byid(user_id: int) -> UserModel:
    return await service.get_user_byid(user_id)
@app.delete("/users/{user_id}", tags=["Users"])
async def delete_user(user_id: int) -> bool:
    return await service.delete_user(user_id)
@app.post("/users/", tags=["Users"])
async def set_user(user: UserModel) -> bool:
    return await service.set_user(user)
@app.put("/users/", tags=["Users"])
async def upd_user(user: UserModel) -> bool:
    return await service.upd_user(user)
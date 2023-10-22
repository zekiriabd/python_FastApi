from typing import List, Annotated

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from fastapi.responses import HTMLResponse

from app.Models.UserModel import CredentialModel, UserModel
from app.Services.JwtTokenAuthentication import generate_token, authorize_admin, authorize
from app.Services.UserServices import UserServices

app = FastAPI(title="My App Name", description="My description", version="0.0.1")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@app.post("/token/", tags=["Users"])
async def get_Token(credential: CredentialModel, user_service: UserServices = Depends()) -> str:
    token = generate_token(credential, user_service)
    return token


@app.get("/users/", tags=["Users"])
async def get_users(token: Annotated[str, Depends(oauth2_scheme)],
                    user_service: UserServices = Depends()) -> List[UserModel]:
    if authorize_admin(token):
        return await user_service.get_users()

    
@app.get("/users/", tags=["Admin Users"])
async def get_users(token: Annotated[str, Depends(oauth2_scheme)],
                    user_service: UserServices = Depends()) -> List[UserModel]:
    if authorize(token):
        return await user_service.get_users()

@app.get("/users/", tags=["Admin Users"])
async def get_users(token: Annotated[str, Depends(oauth2_scheme)],
                    user_service: UserServices = Depends()) -> List[UserModel]:
    if authorize(token):
        return await user_service.get_users()


@app.get("/users/{user_id}", tags=["Users"])
async def get_user_byid(user_id: int,
                        token: Annotated[str, Depends(oauth2_scheme)],
                        user_service: UserServices = Depends()) -> UserModel:
    if authorize_admin(token):
        return await user_service.get_user_byid(user_id)


@app.delete("/users/{user_id}", tags=["Users"])
async def delete_user(user_id: int,
                      token: Annotated[str, Depends(oauth2_scheme)],
                      user_service: UserServices = Depends()) -> dict[str, str]:

    if authorize_admin(token):
        await user_service.delete_user(user_id)

@app.post("/users/", tags=["Users"])
async def set_user(user: UserModel,
                   token: Annotated[str, Depends(oauth2_scheme)],
                   user_service: UserServices = Depends()) -> dict[str, str]:
    if authorize(token):
        if await user_service.set_user(user):
            return {"message": "Ok"}
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="هذالسحل موجود مسبقا")


@app.put("/users/", tags=["Users"])
async def upd_user(user: UserModel,
                   token: Annotated[str, Depends(oauth2_scheme)],
                   user_service: UserServices = Depends()) -> dict[str, str]:
    if authorize_admin(token):
        if await user_service.upd_user(user):
            return {"message": "Ok"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="هذا السجل الذي تريد تغييره غير موجود")




@app.get("/")
async def read_root():
    return HTMLResponse("<h1>My Application</h1> "
                        "<p> Description</p> "
                        "<a href='/docs'>Swagger Documentation click</a>")


"""
 @app.get("/")
async def read_root():
    # Data to pass to the template
    data = {"title": "My Application", "content": "Hello, World!"}
    # Render the template and pass data to it
    return TemplateResponse("index.html", {"request": "request", "data": data})
    
"""


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080 )
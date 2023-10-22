from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette import status

security = HTTPBasic()


def authorize_admin(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == "AdminUserName" and credentials.password == "AdminPass":
        return True
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid Authorization Header",
                            headers={"WWW-Authenticate": "Basic"})


def authorize(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == "MyUserName" and credentials.password == "MyPass":
        return True
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid Authorization Header",
                            headers={"WWW-Authenticate": "Basic"})

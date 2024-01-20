from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException
from starlette import status

from app.Models.User import User
from app.Models.UserDto import CredentialModel, UserDto
from app.Services.UserServices import UserServices

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"


def generate_token(credential: CredentialModel, user_service: UserServices):
    user: User = user_service.get_user_by_credential(credential)
    if user is not None:
        payload = {
            "sub": user.name,
            "exp": datetime.utcnow() + timedelta(minutes=30),
            "roles": user.role
        }
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid Authorization Header",
                            headers={"WWW-Authenticate": "Bearer"})


def authorize_admin(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        role = payload.get("roles")
        if role == "Admin":
            return payload
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid Authorization Header",
                                headers={"WWW-Authenticate": "Basic"})
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


def authorize(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        role = payload.get("roles")
        if role == "User":
            return payload
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid Authorization Header",
                                headers={"WWW-Authenticate": "Basic"})
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

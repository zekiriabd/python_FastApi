from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from starlette import status

ApiKey_value = "6CBxzdYcEgNDrRhMbDpkBF7e4d4Kib46dwL9ZE5egiL0iL5Y3dzREUBSUYVUwUkN"

def authorize(header_value: str = Depends(APIKeyHeader(name="ApiKey"))):
    if header_value == ApiKey_value:
       return True
    else:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid Authorization Header",
                                headers={"WWW-Authenticate": "Basic"})
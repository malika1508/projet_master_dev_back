
import utils
from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi.param_functions import Depends
from fastapi import status
from fastapi.exceptions import HTTPException
from jose import JWTError, jwt
from typing import Union
from datetime import datetime, timedelta
from utils import *
from jose import JWTError, jwt
from config import settings


oauth2_scheme  = OAuth2PasswordBearer(tokenUrl= 'login')

def create_access_token(data: dict):
    new_data = data.copy()
    new_data['exp'] = datetime.utcnow()+ timedelta(minutes= settings.ACCESS_TOKEN_EXPIRE_TIME)
    token = jwt.encode(claims= new_data, key= settings.SECRET_KEY, algorithm= settings.ALGORITHM)
    return token


def get_current_user_id(token : str = Depends(oauth2_scheme)):
    try :
        payload =  jwt.decode(token = token, key = settings.SECRET_KEY, access_token = "JWT", algorithms= [settings.ALGORITHM])
        if payload.get("id"):
            return payload.get("id")
        else :
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials : user not found", 
            headers={"WWW-Authenticate": "Bearer"}
        )
    except JWTError as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= e, 
            headers={"WWW-Authenticate": "Bearer"}
        )
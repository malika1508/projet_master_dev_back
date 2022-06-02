
# import sys
# sys.path.append('../')

from fastapi import APIRouter,  status, HTTPException, Depends
from fastapi.security.oauth2 import  OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import utils as utils
from schemas import Animateur_login, Token
from database import get_db
import models as models
from jwt_stuff import create_access_token
from typing import Union

router = APIRouter()

@router.post("/login/")
def login(user_credentials: Animateur_login, db: Session = Depends(get_db)):
    user : Union[models.Animateur, None] = db.query(models.Animateur).filter(models.Animateur.phone_num == user_credentials.phone_num).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "user not found")
    if utils.encrypt(user_credentials.password) != user.password: 
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "user not found")
    token = create_access_token({
        "id" : user.id,
        "phone_num" : user.phone_num
    })
    return {"access_token" :token, "token_type" : "bearer"}


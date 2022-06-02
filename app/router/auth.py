
# import sys
# sys.path.append('../')

from fastapi.routing import APIRouter
from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
import app.utils as utils
from app.schemas import Animateur_login
from app.database import get_db
import app.models as models
from app.jwt_stuff import create_access_token
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


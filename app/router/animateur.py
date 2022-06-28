from fastapi import status
from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Union
from app.utils import encrypt
from app.database import get_db
from app.schemas import Animateur, Animateur_Res
from app.jwt_stuff import get_current_user_id
import app.models as models

router = APIRouter()

# get all animateurs
@router.get('/animateur/list', response_model = List[Animateur_Res] , tags= ['animateur'])
async def get_all_animateur(db:Session = Depends(get_db)):
    return db.query(models.Animateur).all()

#get the current animateur
@router.get('/animateur/', response_model = Animateur_Res  , tags= ['animateur'])
async def get_animateur(id: int = Depends(get_current_user_id),  db:Session = Depends(get_db)):
    return db.query(models.Animateur).filter(models.Animateur.id == id).first()

# check the visit of the pos_id to_day
@router.put("/animateur/{id_pos}")
async def check_a_visit(
    id_pos : int,  
    db :Session = Depends(get_db), 
    id : int = Depends(get_current_user_id), 
    tags = ['animateur'],
    status_code = 204, 
):
    print(id, id_pos, datetime.now().date())
    query = db.query(models.Visit).filter(models.Visit.id_anim == id).\
                                    filter(models.Visit.id_pos == id_pos).\
                                    filter(models.Visit.date_visit == datetime.now().date())
    visit : Union[models.Visit , None] = query.first()
    if visit == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"no such visit")
    else:
        visit.checked = True
        db.commit()

    return

# add animateur
@router.post("/animateur/",
            status_code = status.HTTP_201_CREATED, 
            response_model = Animateur_Res,  
            tags= ['animateur']
)
async def add_animateur(payload : Animateur, db:Session = Depends(get_db) ):
    
    db_user = models.Animateur(
        full_name = payload.full_name,
        password =  encrypt(payload.password),
        phone_num = payload.phone_num,
        zone = payload.zone, 
        last_day = payload.last_day,
        max_days = payload.max_days
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

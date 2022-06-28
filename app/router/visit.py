from fastapi.routing import APIRouter
from fastapi.param_functions import Depends
from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from app.database import get_db
import app.models as models
from app.schemas import Visit
from app.jwt_stuff import get_current_user_id

router = APIRouter()

# get plan de visit of the current animateur
@router.get("/plan/", tags=['visit'])
def get_list_visits( id: int = Depends(get_current_user_id),db: Session = Depends(get_db), tags = ['visit']):
    visits =  db.query(models.Visit, models.Pos).\
        filter( models.Pos.id == models.Visit.id_pos).\
        filter(models.Visit.id_anim == id).\
        all()
    res = []
    for visit in visits:
        record = {}
        record['day'] = visit[0].day
        record['phone_num'] = visit[1].phone_num
        record['x'] = visit[1].x
        record['y'] = visit[1].y
        res.append(record)
        
    return res



# get plan de visit d'aujourd'hui
@router.get("/plan/today", tags=['visit'])
def get_list_visits_today(db: Session = Depends(get_db), id: int = Depends(get_current_user_id), tags = ['visit']):
    anim : models.Animateur= db.query(models.Animateur).filter(models.Animateur.id == id).first()

    day = anim.last_day 
    visits =  db.query(models.Visit, models.Pos).\
        filter(models.Visit.id_anim == id).\
        filter(models.Visit.day == day).\
        filter( models.Pos.id == models.Visit.id_pos).\
        all()

    results = []
    for visit in visits:
        v = visit[1].__dict__
        v['day'] = visit[0].day
        results.append(v)
    return results

    
# get all plan de visits
@router.get("/plan/all",response_model = List[Visit], tags=['visit'])
def get_visits_all(db: Session = Depends(get_db)):
    return db.query(models.Visit).all()

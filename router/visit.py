import sys
sys.path.append('../')

from fastapi import APIRouter, Depends
from datetime import date, datetime
from typing import List
from sqlalchemy.orm import Session
from database import get_db
import models as models
from schemas import Visit
from jwt_stuff import get_current_user_id

router = APIRouter()

# get plan de visit of the current animateur
@router.get("/plan/", tags=['visit'])
def get_list_visits( id: int = Depends(get_current_user_id),db: Session = Depends(get_db), tags = ['visit']):
    visits =  db.query(models.Visit, models.Pos).\
        filter( models.Pos.id == models.Visit.id_pos).\
        filter(models.Visit.id_anim == id).\
        all()

    return visits



# get plan de visit d'aujourd'hui
@router.get("/plan/today", tags=['visit'])
def get_list_visits_today(db: Session = Depends(get_db), id: int = Depends(get_current_user_id), tags = ['visit']):
    visits =  db.query(models.Visit, models.Pos).\
        filter(models.Visit.id_anim == id).\
        filter(models.Visit.date_visit == datetime.utcnow().date()).\
        filter( models.Pos.id == models.Visit.id_pos).\
        all()

    results = []
    for visit in visits:
        v = visit[1].__dict__
        v['id_pos'] = visit[0].id_pos
        v['date_visit'] = visit[0].date_visit
        v['checked'] = visit[0].checked
        results.append(v)
    return results

    
# get all plan de visits
@router.get("/plan/all",response_model = List[Visit], tags=['visit'])
def get_visits_all(db: Session = Depends(get_db)):
    return db.query(models.Visit).all()

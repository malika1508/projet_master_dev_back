# import sys
# sys.path.append('../')

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from database import get_db
import models as models
from schemas import Pos, Pos_Res
from typing import List


router = APIRouter()



@router.get("/pos",response_model= List[Pos_Res], tags=['pos'])
async def get_list_pos(db: Session = Depends(get_db)):
    pdvs = db.query(models.Pos).all()
    return pdvs

@router.get("/pos/{id}",response_model= Pos_Res, tags=['pos'])
async def get_pos(id: int, db: Session = Depends(get_db)):
    return db.query(models.Pos).filter(models.Pos.id== id).first()

@router.post("/pos/",  status_code= status.HTTP_201_CREATED, response_model = Pos_Res ,tags=['pos'])
async def post_pos(payload : Pos, db: Session = Depends(get_db)):
    db_pos = models.Pos(**payload.dict())
    db.add(db_pos)
    db.commit()
    db.refresh(db_pos)
    return db_pos


from datetime import date
from pydantic import BaseModel
from typing import Union

# are used for routing
class Pos (BaseModel):
    phone_num : str
    x : int
    y : int
    zone : int
    priority : int
    class Config:
        orm_mode = True

class Pos_Res(BaseModel):
    id : int    
    phone_num : str
    x : int
    y : int
    zone : int
    priority : int
    class Config:
        orm_mode = True

class Animateur(BaseModel):
    phone_num : str
    full_name : str
    password : str
    zone : int
    class Config:
        orm_mode = True

class Animateur_Res(BaseModel):
    id : int
    phone_num : str
    full_name : str
    password : str
    zone : int
    class Config:
        orm_mode = True

class Animateur_login(BaseModel):
    phone_num : str
    password : str
    class Config:
        orm_mode = True

class Visit(BaseModel):
    id_pos : int
    id_anim : int
    date_visit : date
    checked : bool
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id : int
    phone_num: Union[str, None] = None
    exp : int

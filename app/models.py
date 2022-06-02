from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean
from app.database import Base

# used for db (creating tables)
class Pos(Base):
    __tablename__ = "pos"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    phone_num = Column(String)
    x = Column(Integer, nullable = False)
    y = Column(Integer, nullable = False)
    zone = Column(Integer)
    priority = Column(Integer, nullable = False)

class Animateur(Base):
    __tablename__ = "animateur"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    phone_num = Column(String, nullable = False)
    full_name = Column(String)
    password = Column(String, nullable = False)
    zone = Column(Integer, nullable = False)

class Visit(Base):
    __tablename__ = 'visit'
    __table_args__ = {'extend_existing': True}

    id_pos  = Column(Integer,  ForeignKey('pos.id'), primary_key = True)
    id_anim  = Column(Integer, ForeignKey('animateur.id'), primary_key = True)
    date_visit = Column(Date, primary_key = True, nullable = False)
    checked = Column(Boolean, server_default='FALSE')
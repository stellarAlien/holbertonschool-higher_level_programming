#!/usr/bin/python3
"""
create city class that has a relation with state
"""
#int import problem here, 
from sqlalchemy import(Column, ForeignKey, String, Integer)
from model_state import Base, State
from sqlalchemy.orm import declarative_base


Base = declarative_base()

if __name__ == "__main__" :
    class City(Base):
        __tablename__ = "Cities"
        id = Column(Integer=1, Primar_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        state_id = Column(id=Integer nullable=False, ForeignKey(State.id))

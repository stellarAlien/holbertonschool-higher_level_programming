#!/usr/bin/python3
"""
construct tables from base class
ORM Power
"""
from sqlalchemy import (Integer, create_engine, Column, String)
from sqlalchemy.orm import declarative_base
import sys



if __name__ == "__main__":
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], 
    sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base = declarative_base()

    class State(Base):
        """
        ORM repr of states table
        """
        __tablename__ = "states"
        id = Column(Integer, nullable=False, unique=True, Primary_Key=True, autoincrement=True)
        name = Column(String(128), nullable=False)

#!/usr/bin/python3
"""
starting to harvest orm power
"""
from model_state import Base, State
import sys
from sqlalchemy import engine, create_engine, query
from sqlalchemy.orm import sessionmaker, Error


if __name__ == "__main__":
    """
    search state by name
    """
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user, passwd, db), 
    pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session=sessionmaker(bind=engine)

    try:
        nm =session.query.filter_by(id=2).first()
        nm.name = "New Mexico"
        session.commit()
    except Error as e:
        print(e)
    session.close()

#!/usr/bin/python3
"""
starting to harvest orm power
"""
from model_state import Base, State
import sys
from sqlalchemy import engine, create_engine, query
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    get state by state id
    """
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user, passwd, db), 
    pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session=sessionmaker(bind=engine)
    
    try:
        name = str(str(sys.argv[4]))
    except:
        print("name doesn't figure in the command")
    try:
        state = session.query().filter_by(name=str(sys.argv[4])).first()
        if state:
            print("{:d}".format(State.id))
    except:
        print("Not found")
    session.close()
#!/usr/bin/python3
"""
starting to harvest orm power
"""
from model_state import Base, State
import sys
from sqlalchemy import engine, create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), 
    pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session=sessionmaker(bind=engine)
    #ORM query to list all state objects
    try:
        state = session.query(State).order_by(State.id).first()
        print("{:d}: {:s}".format(state.id, state.name))
    except:
        print("Nothing")
    session.close()
    
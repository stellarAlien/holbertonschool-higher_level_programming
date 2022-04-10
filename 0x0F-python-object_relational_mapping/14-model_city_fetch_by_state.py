#!/usr/bin/python3
"""
print all City objects from hbtn_0e_14_usa
"""
from model_state import Base, State
from model_city import City
import sys
from sqlalchemy import engine, create_engine
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user, passwd, db), 
    pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session=sessionmaker(bind=engine)
    city = session.query(State.name, City.id, City.name).filter_by(State.id == City.state_id).order_by(City.id)
    for row in city:
        print("{:s}: ({:d}) {:s}".format(row[0], row[1], row[2]))
    session.close()




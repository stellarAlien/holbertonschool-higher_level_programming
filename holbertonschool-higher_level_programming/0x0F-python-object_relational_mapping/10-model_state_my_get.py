#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""


import sqlalchemy
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    first = session.query(State).first()
    if (first is not None):
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    session.close()

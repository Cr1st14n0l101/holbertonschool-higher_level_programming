#!/usr/bin/python3
"""
    Prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from model_state import Base, State


if __name__ == "__main__":
    state_object, counter = sys.argv[4], 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    names = session.query(State).order_by(State.id).all()
    for row in range(len(names)):
        if names[row].name == state_object:
            counter += 1
            print("{}".format(names[row].id))
    if counter == 0:
        print("Not found")
    session.close()

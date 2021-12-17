#!/usr/bin/python3
"""
    Adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from sqlalchemy.sql.expression import update
from model_state import Base, State


if __name__ == "__main__":
    counter = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    current_state = session.query(State).filter_by(id=2).first()
    current_state.name = 'New Mexico'
    session.add(current_state)
    session.commit()
    session.close()

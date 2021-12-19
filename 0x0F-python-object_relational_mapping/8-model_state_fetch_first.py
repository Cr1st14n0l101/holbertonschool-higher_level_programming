#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    names = session.query(State).order_by(State.id).first()
    print(
        "Nothing" if not names else "{}: {}"
        .format(names.id, names.name)
        )
    session.close()

#!/usr/bin/python3
"""
    Deletes all State objects with
    a name containing the letter a from the
    database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import Session
from sqlalchemy import engine, create_engine
from sqlalchemy.sql.functions import user
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    results = session.query(State, City).join(City).all()
    for row_state, row_city in results:
        print('{}: ({}) {}'.format(row_state.name, row_city.id, row_city.name))
    session.close()

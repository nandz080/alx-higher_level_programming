#!/usr/bin/python3
""" Module deletes all state objects with name containing letter a
        from db hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    sessionMaker = sessionmaker(bind=engine)
    session = sessionMaker()

    del_states = session.query(State).filter(State.name.like('%a%')).all()
    for state in del_states:
        session.delete(state)

    session.commit()

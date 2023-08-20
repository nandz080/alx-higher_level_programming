#!/usr/bin/python3
""" module adds state objet "Louisiana" to db hbtn_0e_6_usa
"""

import sys
from unicodedata import name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    sessionMaker = sessionmaker(bind=engine)
    session = sessionMaker()

    addedObject = State(name="Louisiana")
    session.add(addedObject)
    session.commit()
    print(addedObject.id)

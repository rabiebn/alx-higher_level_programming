#!/usr/bin/python3
"""Lists all State objects from DB hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for row in session.query(State).order_by(State.id_state).all():
        print("{}: {}".format(row.id_state, row.name))

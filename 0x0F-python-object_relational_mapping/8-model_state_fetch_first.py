#!/usr/bin/python3
"""Lists the first State object from DB hbtn_0e_6_usa
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

    try:
        state = session.query(State).first()
        print("{}: {}".format(state.id, state.name))
    except Exception as e:
        print("Nothing")

#!/usr/bin/python3
"""
Adds a State object to states table in DB hbtn_0e_6_usa.
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, exc

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_la = State('Louisiana')
    session.add(state_la)
    session.commit()
    print(state_la.id)

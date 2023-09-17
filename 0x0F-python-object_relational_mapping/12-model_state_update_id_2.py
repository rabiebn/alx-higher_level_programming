#!/usr/bin/python3
"""
Updates State name in states table in DB hbtn_0e_6_usa.
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

    state = session.query(State).filter(State.id == 2).update({
        'name': 'New Mexico'})
    session.commit()

    """
    # 2nd method to update an entry:
    state = session.query(State).filter(State.id == 2).one()
    state.name = 'New Mexico'
    session.commit()
    """

#!/usr/bin/python3
"""
Deletes State objs in states table with 'a' in the name in DB hbtn_0e_6_usa.
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

    del_state = session.query(State).filter(State.name.like('%a%')).delete(
            synchronize_session=False)
    session.commit()

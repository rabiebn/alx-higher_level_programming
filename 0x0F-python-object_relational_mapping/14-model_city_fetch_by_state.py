#!/usr/bin/python3
"""
Prints all objects from DB hbtn_0e_14_usa.
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    city_state = session.query(State, City).join(State).order_by(
            City.id_city).all()
    for row in city_state:
        print("{}: ({}) {}".format(row[0].name, row[1].id_city, row[1].name))

#!/usr/bin/python3
"""model_state describes State class"""

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """
    State class mapped to table states in hbtn_0e_6_usa
    """
    __tablename__ = "states"
    id_state = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(length=128))

    def __init__(self, name):
        """
        Initialize State objects
        """
        self.name = name

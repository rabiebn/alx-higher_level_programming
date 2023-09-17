#!/usr/bin/python3
"""model_state describes State class"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class mapped to table states in hbtn_0e_6_usa
    """
    __tablename__ = "states"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(length=128), nullable=False)

    def __init__(self, name):
        """
        Initialize State objects
        """
        self.name = name

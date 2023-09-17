#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
"""
model_city defines City class.
"""


class City(Base):
    """
    City class
    """
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey("states.id"))

    def __init__(self, name):
        """
        Initialize City objs
        """
        self.name = name

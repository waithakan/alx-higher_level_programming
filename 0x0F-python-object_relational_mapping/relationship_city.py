#!/usr/bin/python3
"""
Desc: contains the class definition of a City
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base


class City(Base):
    """
    An SQL table called cities
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

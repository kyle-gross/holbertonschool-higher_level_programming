#!/usr/bin/python3
"""This module contains the class City"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from model_state import State

Base = declarative_base()


class City(Base):
    """This is the City class"""
    __tablename__ = "cities"

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

#!/usr/bin/python3
"""This module lists items in the state table"""
from model_state import Base, State
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3],
                                   pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()

    for c, s in session.query(City, State)\
                       .filter(City.state_id == State.id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))

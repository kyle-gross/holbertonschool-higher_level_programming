#!/usr/bin/python3
"""This module lists items in the state table"""
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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

    states = session.query(State).first()

    if states:
        print("{}: {}".format(states.id, states.name), end="")

    print()

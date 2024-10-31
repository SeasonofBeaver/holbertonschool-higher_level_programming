#!/usr/bin/python3

"""lists all state objects from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql username = argv[1]
    mysql password = argv[2]
    database name = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{mysql username}:{mysql password}@localhost:3306/'
        f'{database name}'
        )
    Session = sessionmaker(bind=engine)

    states = Session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    Session.close()

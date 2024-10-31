#!/usr/bin/python3

"""lists all state objects from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = argv[1]
    passw = argv[2]
    db = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{passw}@localhost:3306/'
        f'{db}'
        )
    Session = sessionmaker(bind=engine)

    states = Session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    Session.close()

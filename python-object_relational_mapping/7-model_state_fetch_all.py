#!/usr/bin/python3

"""lists all state objects from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/'
        f'{database_name}'
        )
    Session = sessionmaker(bind=engine)

    states = Session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    Session.close()

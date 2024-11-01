#!/usr/bin/python3

"""lists the searched state from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/'
        f'{database_name}'
        )
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.name == sys.argv[4]).first()

    if states:
        print(states.id)
    else:
        print("Not found")

    session.close()

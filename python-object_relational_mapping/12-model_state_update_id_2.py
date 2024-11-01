#!/usr/bin/python3

"""changes the name of a state to New Mexico."""

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

    updatedState = session.query(State).filter_by(id=2).first()

    if updatedState:
        updatedState.name = "New Mexico"
        session.commit()

    session.close()

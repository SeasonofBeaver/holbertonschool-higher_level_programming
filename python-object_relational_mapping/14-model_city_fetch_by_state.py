#!/usr/bin/python3

"""prints all the Cities in the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    cities = (session.query(City, State).filter(City.state_id == State.id)
        .order_by(City.id).all())

    for city in cities:
        print("%s: (%s) %s", (state.name, city.id, city.name))

    session.close()

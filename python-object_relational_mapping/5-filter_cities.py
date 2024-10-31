#!/usr/bin/python3

"""lists all cities from a specific state."""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities WHERE cities.state = %s \
                    ORDER BY cities.id ASC", (sys.argv[4],))
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()

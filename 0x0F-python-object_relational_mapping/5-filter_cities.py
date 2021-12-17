#!/usr/bin/python3
"""
    Ctakes in the name of a state as an argument and lists
    all cities of that state, using the database
    hbtn_0e_4_usa, no injections
"""
import MySQLdb
import sys


if __name__ == '__main__':

    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
        )
    cursor = db.cursor()
    cursor.execute(
        """SELECT cities.name
        FROM cities INNER JOIN states
        ON state_id=states.id
        WHERE states.name=%s
        ORDER BY states.id ASC""",
        (state_name,)
        )
    table = cursor.fetchall()
    for row in range(len(table)):
        print(table[row][0], end="")
        if row != len(table) - 1:
            print(", ", end="")
    print("")

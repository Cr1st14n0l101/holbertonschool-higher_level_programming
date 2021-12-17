#!/usr/bin/python3
"""
    Connect to the hbtn_0e_0_usa database and print the cities
    with if matches with a given argument, no injections
"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
        )
    cursor = db.cursor()
    cursor.execute(
        """SELECT cities.id,cities.name, states.name
        FROM cities INNER JOIN states
        ON state_id=states.id
        ORDER BY id ASC"""
        )
    table = cursor.fetchall()
    for row in table:
        print(row)

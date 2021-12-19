#!/usr/bin/python3
"""
    Connect to the hbtn_0e_0_usa database and print the states
    with if matches with a given argument
"""
import MySQLdb
import sys


if __name__ == '__main__':

    new_argument = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
        )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(
            new_argument)
            )
    table = cursor.fetchall()
    for row in table:
        print(row)

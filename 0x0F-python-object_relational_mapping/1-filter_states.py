#!/usr/bin/python3
"""
    Connect to the hbtn_0e_0_usa database and print the states
    with a name starting with N
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    table = cursor.fetchall()
    for row in table:
        if row[1][0] == 'N':
            print(row)

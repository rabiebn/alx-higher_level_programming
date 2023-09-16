#!/usr/bin/python3
"""
lists all cities from the DB hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    with db.cursor() as cur:
        cur.execute("""
                    SELECT cities.id, cities.name, states.name
                    FROM cities
                    INNER JOIN states
                    ON cities.state_id = states.id
                    ORDER BY cities.id;
                    """)
        states = cur.fetchall()
    for row in states:
        print(row)

    db.close()

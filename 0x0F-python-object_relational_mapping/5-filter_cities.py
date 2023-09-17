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
                    SELECT cities.name
                    FROM cities
                    INNER JOIN states
                    ON cities.state_id = states.id
                    WHERE states.name = %(state)s
                    ORDER BY cities.id;
                    """, {
                        'state': argv[4],
                        })
        states = cur.fetchall()
        try:
            for row in states[0:-1]:
                print(row[0], end=', ')
            print(states[-1][0])
        except Exception as e:
            print('')


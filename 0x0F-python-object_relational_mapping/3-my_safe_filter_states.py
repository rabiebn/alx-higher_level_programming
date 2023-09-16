#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument, safe from SQL injection.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    with db.cursor() as cur:
        cur.execute("""
                    SELECT * FROM states
                    WHERE name = %(name)s
                    ORDER BY id
                    """, {
                        'name': sys.argv[4]
                        })
        states = cur.fetchall()
    for row in states:
        print(row)
    cur.close()
    db.close()

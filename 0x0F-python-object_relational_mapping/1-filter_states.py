#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute('SELECT * FROM states')
    states = cur.fetchall()
    for row in states:
        if row[1].startswith('N'):
            print(row)
    cur.close()
    db.close()

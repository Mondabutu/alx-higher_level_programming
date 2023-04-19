#!/usr/bin/python3
"""
Display all values in the states table of the database hbtn_0e_0_usa whose name matches that supplied as argument.
Usage: ./2-my_filter_states.py <mysql username> \
                                <mysql password> \
                                <database name> \
                                <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    dbs = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost", passwd=sys.argv[2], dbs=sys.argv[3])
    cn = db.cursor()
    cn.execute("SELECT * FROM sates WHERE name LIKE '{:s}' ORDER BY \ is ASC".format(sys.agrv[4]))
    states = cn.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    cn.close()
    dbs.close()

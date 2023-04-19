#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql username> \
                            <mysql password> \
                            <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    dbs = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], dbs=sys.argv[3])
    cn = db.cursor()
    cn.execute("SELECT * FROM `states` ORDER by `id`")
    [print(state) for state in cn.fetchall() if state[1][0] == "N"]

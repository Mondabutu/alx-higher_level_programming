#!/usr/bin/python3
"""
Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
Usage: ./4-cities_by_state.py <mysql username> \
                              <mysql password> \
                              <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    dbs = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], dbs=sys.argv[3])
    cn = db.cursor()
    cn.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    [print(city) for city in cn.fetchall()]

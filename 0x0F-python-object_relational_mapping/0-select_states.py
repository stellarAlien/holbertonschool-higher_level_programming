#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
from mysql.connector import Error
import MySQLdb
import sys

if __name__ == "__main__":
    """
    connect to hbtn_0e_0_usa and list
    all the states
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    #set cursor
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()

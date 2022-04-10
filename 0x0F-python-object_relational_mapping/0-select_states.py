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
    try:
        connect = MySQLdb.connector.connect(host="localhost",
                                            user=sys.argv[1],
                                            password=sys.argv[2],
                                            database=sys.argv[3],
                                            port="3306")
        cursor = connect.cursor()
    except Error as e:
        print(e)
    # query to list all state names
    query = ("SELECT * FROM states ORDER BY name;")
    try:
        cursor.execute(query)
        connect.commit()
        stt = cursor.fetchall()
        for row in stt.fetchall():
            print("({:d}, {:s})".format(row[0], row[1]))
    except Error as e:
        print(e)
    finally:
        cursor.close()
        connect.close()

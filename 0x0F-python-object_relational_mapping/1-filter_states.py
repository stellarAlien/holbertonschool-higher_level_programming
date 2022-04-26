#!/usr/bin/python3

from mysql.connector import Error
import MySQLdb
import sys
if __name__ == "main":
    """
    execute 
    """
    try:
        connect = MySQLdb.connector.connect(host="localhost", 
        user = sys.argv[1]), 
        password = sys.argv[2]), database= str(sys.argv[3]), port = 3306)
        cursor = connect.cursor()
    except Error as e:
        print(e)
    # query to list all state names starting with N
    query = ("SELECT name from states WHERE name like 'N%';")
    try:
        cursor.execute(query)
        connect.commit()
        stt = cursor.fetchall()
        for row in stt:
            print(row)
    except Error as e:
            print(e)
    finally:
        cursor.close()
        connect.close()
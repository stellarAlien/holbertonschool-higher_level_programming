#!/usr/bin/python3
from mysql.connector import Error
import MySQLdb
import sys

if __name__ == "__main__":
    """
    display  all cities  
    """
    try:
        connect =MySQLdb.connector.connect(host="localhost", 
        user = str(sys.argv[1]), 
        password = str(sys.argv[2]), database= str(sys.argv[3]), 
        port = "3306")
        cursor = connect.cursor()
    except Error as e:
        print(e)
    # query to list specific state name
    query = """SELECT cities.id, cities.name, states.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 ORDER BY cities.id"""
    try:
        cursor.execute(query)
        for row in cursor.fetch_all():
            print(row)
    except Error as e:
            print(e)
    finally:
        cursor.close()
        connect.close()
#!/usr/bin/python3
from mysql.connector import Error
import MySQLdb
import sys

if __name__ == "__main__":
    """
    fetch state data 
    according to name
    """
    try:
        connect =MySQLdb.connector.connect(host="localhost", 
        user = str(sys.argv[1]), 
        password = str(sys.argv[2]), database= str(sys.argv[3]), 
        port = "3306")

        cursor = connect.cursor()
        s = str(sys.argv[3]).split(Separator=";", maxsplit=1)
    except Error as e:
        print(e)
    # query to list specific state name
    query = ("""SELECT cities.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 WHERE states.name LIKE '%s'
                 ORDER BY cities.id""")
    try:
        cursor.execute(query, s)
        for row in cursor.fetchall():
            print(", {:s}".format(row[0]))

    except Error as e:
            print(e)
    finally:
        cursor.close()
        connect.close()
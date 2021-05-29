#!/usr/bin/python3
"""Lists all cities that from the hbtn_0e_0_usa database"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db_connection = MySQLdb.connect('localhost',
                                    argv[1],
                                    argv[2],
                                    argv[3])

    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM cities')

    cities = cursor.fetchall()

    for i in range(len(cities)):
        print(cities[i])

#!/usr/bin/python3
"""Lists all states that start with 'N' from the hbtn_0e_0_usa database"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db_connection = MySQLdb.connect('localhost',
                                    argv[1],
                                    argv[2],
                                    argv[3])

    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM states')

    states = cursor.fetchall()

    for i in range(len(states)):
        if (states[i][1] startswith('N')):
            print(states[i])

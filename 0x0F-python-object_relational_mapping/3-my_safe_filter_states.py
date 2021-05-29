#!/usr/bin/python3
"""Safely lists all states that match argv[4] from the database"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db_connection = MySQLdb.connect('localhost',
                                    argv[1],
                                    argv[2],
                                    argv[3])

    cursor = db_connection.cursor()
    with db_connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name = BINARY %(name)s
            """, {
                'name': argv[4]
            })

        states = cursor.fetchall()

    for i in range(len(states)):
        print(states[i])

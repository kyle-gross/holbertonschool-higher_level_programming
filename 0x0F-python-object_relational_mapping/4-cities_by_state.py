#!/usr/bin/python3
"""Lists all cities that from the hbtn_0e_0_usa database"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db_connection = MySQLdb.connect('localhost',
                                    argv[1],
                                    argv[2],
                                    argv[3])

    with db_connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                cities.id,
                cities.name,
                states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            """)

        cities = cursor.fetchall()

    for i in range(len(cities)):
        print(cities[i])

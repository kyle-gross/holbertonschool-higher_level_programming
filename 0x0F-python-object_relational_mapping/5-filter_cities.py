#!/usr/bin/python3
"""
Safely lists all cities from the hbtn_0e_0_usa database
that match the state specified by argv[4]
"""


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
                cities.name
            FROM
                states
            JOIN
                cities
            ON
                states.id = cities.state_id
            WHERE
                states.name = BINARY %(states)s
            """, {
                'states': argv[4]
            })

        cities = cursor.fetchall()

    for i in range(len(cities)):
        print(cities[i][0], end="")
        if i < (len(cities) - 1):
            print("", end=", ")

    print()

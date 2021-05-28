#!/usr/bin/python3
"""Lists all statesfrom the hbtn_0e_0_usa database"""
from sys import argv
import MySQLdb


db_connection = MySQLdb.connect('localhost',
                                argv[1],
                                argv[2],
                                argv[3])

cursor = db_connection.cursor()
cursor.execute('SELECT * FROM states')

states = cursor.fetchall()

print(states)

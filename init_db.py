import sqlite3

connection = sqlite3.connect('database.db')

# create empty tables
with open('schema.sql') as f:
    connection.executescript(f.read())

# fill tables with test data
cur = connection.cursor()

# Roles
cur.execute('INSERT INTO Roles (name) VALUES (?)', ('admin',))
cur.execute('INSERT INTO Roles (name) VALUES (?)', ('user',))

# Users
# for i in range(10):
#     cur.execute('INSERT INTO Users (), VALUES ()', ('',))

connection.commit()
connection.close()


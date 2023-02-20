import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute('INSERT INTO Roles (name) VALUES (?)', ('admin',))
cur.execute('INSERT INTO Roles (name) VALUES (?)', ('user',))

connection.commit()
connection.close()

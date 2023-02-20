import sqlite3

connection = sqlite3.connect('database.db')
cur = connection.cursor()

print('Roles:', cur.execute('select * from Roles').fetchall())
# print('Users:', cur.execute('select * from Users').fetchall())

connection.commit()
connection.close()

import sqlite3

connection = sqlite3.connect('database.db')
cur = connection.cursor()

tables = ['Roles', 'Users', 'Texts', 'Tags', 'Fandoms', 'Permissions']

for table in tables:
    print(f'{table}:', cur.execute(f'select * from {table}').fetchall(), '\n')

connection.commit()
connection.close()

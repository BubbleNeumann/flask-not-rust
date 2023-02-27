import sqlite3
from app.models import User

connection = sqlite3.connect('database.db')
cur = connection.cursor()

tables = ['Roles', 'Users', 'Texts', 'Tags', 'Fandoms', 'Permissions']

for table in tables:
    print(f'{table}:', cur.execute(f'select * from {table}').fetchall(), '\n')

connection.commit()

"""Tests for the second check point"""

test_user = User(*cur.execute('select * from Users where id = 3').fetchall()[0])

# test User constructor and __repr__ overload
print(test_user)

# test User get_texts()
print(test_user.get_texts())

# test User delete_from_db()
test_user.delete_from_db()
users = cur.execute('select * from Users').fetchall()
print(users)

connection.close()

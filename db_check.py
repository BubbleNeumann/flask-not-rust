import sqlite3
from app.models import User, Text

connection = sqlite3.connect('database.db')
cur = connection.cursor()

tables = ['Roles', 'Users', 'Texts', 'Tags', 'Fandoms', 'Permissions', 'Texts_Users']

for table in tables:
    print(f'{table}:', cur.execute(f'select * from {table}').fetchall(), '\n')

# connection.commit()

"""Tests for the second check point"""

# test User constructor and __repr__ overload
# test_user = User(*cur.execute('select * from Users where id = 3').fetchone())
# print(test_user)

# test User get_texts()
# print(test_user.get_texts())

# test Text constructor and __repr__ overload
# test_text = Text(*cur.execute('select * from Texts').fetchone())
# print(test_text)
# test_text.delete_from_db(cur=cur)
#
# test_user = User(*cur.execute('select * from Users where id = 3').fetchone())
# print(test_user)

# test User delete_from_db()
# test_user.delete_from_db(cur=cur)
# users = cur.execute('select * from Users').fetchall()
# print(users)

# test User write_to_db()
# test_user = User(*users[0])
# print()
# new_test_user = User(id=None, username='newname', email='newemail', password='pass', role_id='2')
# new_test_user.write_to_db(con=connection)
# print(new_test_user)
# connection.commit()
# print(new_test_user.get_texts())
# users = cur.execute('select * from Users').fetchall()
# print(users)
# new_test_user.delete_from_db(con=connection)
# users = cur.execute('select * from Users').fetchall()
# print(users)
# new_test_user.delete_from_db(cur=cur)
# connection.commit()
# users = cur.execute('select * from Users').fetchall()
#
# print(users)

#
#
# connection.commit()

text = Text.get_text_by_id(2)
print(text.get_fandoms())
# user = User.get_user_by_id(2)
# print(user)


connection.close()

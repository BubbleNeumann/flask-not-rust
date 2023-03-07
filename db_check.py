import sqlite3
from app.models import User, Text, Tag, Fandom

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

# new_test_user = User.get_user_by_id(7)
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

text = Text.get_text_by_id(2)
text.title = "new title"
text.write_to_db(user_id=1)
user = User.get_user_by_id(1)

print(user.get_texts())
# print(text.get_fandoms())
# print(text.get_tags())
# user = User.get_user_by_id(3)
# print(user)
# print(user.get_texts())
#
# print(Tag.get_all_tags())
# print(Fandom.get_all_fandoms())


connection.close()

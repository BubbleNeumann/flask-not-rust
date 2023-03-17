import sqlite3
import sys


def main():
    connection = sqlite3.connect('database.db')

    # create empty tables
    with open('app/schema.sql') as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()


def fill_tables():
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    # Roles
    for role in ['admin', 'user', 'banned']:
        cur.execute('insert into Roles (name) VALUES (?)', (role,))

    # Tags
    cur.execute('INSERT INTO Tags (name, rus_name) VALUES (?, ?)',
                ('Action', 'Приключения'))
    cur.execute('INSERT INTO Tags (name, rus_name) VALUES (?, ?)',
                ('Anime', 'Аниме'))

    # Fandoms
    cur.execute('INSERT INTO Fandoms (name, rus_name) VALUES (?, ?)',
                ('The Witcher', 'Ведьмак'))
    cur.execute('INSERT INTO Fandoms (name, rus_name) VALUES (?, ?)',
                ('Original', 'Ориджинал'))

    # Permissions
    for permis in ['post', 'ban']:
        cur.execute('INSERT INTO Permissions (name) VALUES (?)', (permis,))

    # Roles_Permissions
    # admin can post and ban, user can post, banned has no permissions
    interrel = [('1', '1'), ('2', '1'), ('1', '2')]
    for rel in interrel:
        cur.execute('INSERT INTO Roles_Permissions (permission_id, role_id) VALUES (?, ?)', rel)

    for i in range(5):
        cur.execute('INSERT INTO Users (username, email, password, role_id) VALUES (?, ?, ?, ?)',
                    (f'name{i}', f'email{i}', f'pass{i}', '2'))
        cur.execute('INSERT INTO Texts (title, text_file, release_date, lang, descr, age_restr) VALUES (?, ?, ?, ?, ?, ?)',
                    (f'title{i}', f'path{i}', '2023-02-26', 'eng', 'desc', '13'))

        cur.execute('INSERT INTO Texts_Users (text_id, user_id, is_author) VALUES (?, ?, ?)',
                    (f'{i}', '3', '1'))

        cur.execute('INSERT INTO Texts_Tags (text_id, tag_id) VALUES (?, ?)',
                    (f'{i}', '1'))

        cur.execute('INSERT INTO Texts_Fandoms (text_id, fandom_id) VALUES (?, ?)',
                    (f'{i}', '1'))

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
    if len(sys.argv) > 1 and sys.argv[1] == '--with-data':
        fill_tables()

import sqlite3

class User:
    def __init__(self,  username, email, password, role_id, id=None, critics_att=None) -> None:
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role_id = role_id
        self.critics_att = critics_att

    def update_username_query(self, new_username: str) -> str:
        # on this stage consider new username to be valid
        return f'update Users set username = {new_username} where id = {self.id}'

    def get_texts(self) -> list:
        connection = sqlite3.connect('database.db')
        query = f'select Texts.title from Texts_Users inner join Texts \
            on Texts_Users.text_id = Texts.id where Texts_Users.user_id = {self.id}'
        text_titles = connection.cursor().execute(query).fetchall()
        connection.close()
        return text_titles

    def write_to_db(self, cur=None) -> None:
        """Insert new user into Users"""
        cur_was_passed = True if cur is not None else False
        if cur is None:
            connection = sqlite3.connect('database.db')
            cur = connection.cursor()
        cur.execute('INSERT INTO Users (username, email, password, role_id) VALUES (?, ?, ?, ?)',
                    (self.username, self.email, self.password, self.role_id))
        if not cur_was_passed:
            connection.commit()
            connection.close()

    def delete_from_db(self, cur=None) -> None:
        cur_was_passed = True if cur is not None else False
        if cur is None:
            connection = sqlite3.connect('database.db')
            cur = connection.cursor()

        texts_to_delete = cur.execute(f'select Texts.* from Texts inner join Texts_Users \
                on Texts.id = Texts_Users.text_id where Texts_Users.user_id = {self.id}')

        for text in texts_to_delete:
            Text(*text).delete_from_db(cur=cur)

        cur.execute(f'delete from Users where id = {self.id}')
        if not cur_was_passed:
            connection.commit()
            connection.close()

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.username} {self.email} \
            {"admin" if self.role_id == 1 else ""}'


class Text:
    def __init__(self, id, title, text_file, release_date, lang, descr, age_restr) -> None:
        self.id = id
        self.title = title
        self.text_file = text_file
        self.release_date = release_date
        self.lang = lang
        self.descr = descr
        self.age_restr = age_restr

    def delete_from_db(self, cur=None) -> None:
        cur_was_passed = True if cur is not None else False
        if cur is None:
            connection = sqlite3.connect('database.db')
            cur = connection.cursor()
        cur.execute(f'delete from Texts where id = {self.id}')

        # tables with the same field name
        for table in ['Texts_Users', 'Texts_Tags', 'Texts_Fandoms']:
            cur.execute(f'delete from {table} where text_id = {self.id}')

        if not cur_was_passed:
            connection.commit()
            connection.close()

    def __repr__(self) -> str:
        connection = sqlite3.connect('database.db')
        query = f'select Users.username from Texts_Users inner join Users \
                on Texts_Users.user_id = Users.id where Texts_Users.is_author = 1 \
                and Texts_Users.text_id = {self.id}'
        author = connection.cursor().execute(query).fetchone()[0]
        connection.close()
        return f'{self.__class__.__name__}: {self.title} by {author} published {self.release_date}'
    

class Tag:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    def delete_from_db(self) -> None:
        pass

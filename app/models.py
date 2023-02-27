import sqlite3

class User:
    def __init__(self, id, username, email, password, role_id, critics_att=None) -> None:
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

    def delete_from_db(self) -> None:
        connection = sqlite3.connect('database.db')
        connection.cursor().execute(f'delete from Users where id = {self.id}')
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

    def update_title(self, new_title: str) -> None:
        # return f''
        pass

    def add_tag_query(self, tag_id: int) -> str:
        return f''

    def add_coauthor_query(self, user: User) -> str:
        return f''

    def __repr__(self) -> str:
        # TODO fetch author and fandom
        return f'{self.__class__.__name__}: {self.title}'

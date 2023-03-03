from . import db

class User:
    def __init__(self, id, username, email, password, role_id, critics_att=None) -> None:
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role_id = role_id
        self.critics_att = critics_att

    def get_texts(self) -> list:
        return db.run_select(query=f'select Texts.title from Texts_Users join Texts \
            on Texts_Users.text_id = Texts.id where Texts_Users.user_id = {self.id}')

    def write_to_db(self, con=None) -> None:
         self.id = db.modify_table(query=f'insert into Users (username, email, password, role_id) \
                values ("{self.username}", "{self.email}", "{self.password}", "{self.role_id}")', con=con)

    def add_text(self, text, con=None) -> None:
        text.write_to_db(user_id=self.id, con=con)

    @staticmethod
    def get_user_by_id(id: int):
        return User(*db.run_select(query=f'select * from Users where id = {id}')[0])

    def delete_from_db(self, con=None) -> None:
        texts_to_delete = db.run_select(query=f'select Texts.* from Texts join Texts_Users \
                on Texts.id = Texts_Users.text_id where Texts_Users.user_id = {self.id}')

        for text in texts_to_delete:
            Text(*text).delete_from_db(con=con)

        db.modify_table(query=f'delete from Users where id = "{self.id}"', con=con)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.id} {self.username} {self.email} \
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

    @staticmethod
    def get_text_by_id(id: int):
        return Text(*db.run_select(query=f'select * from Texts where id = {id}')[0])

    def get_tags(self) -> list:
        query = f'select Tags.* from Tags join Texts_Tags \
                on Tags.id = Texts_Tags.tag_id where Texts_Tags.text_id = {self.id}'
        return db.run_select(query=query)

    def get_fandoms(self) -> list:
        query = f'select Tags.name from Tags join Texts_Tags \
                on Tags.id = Texts_Tags.tag_id where Texts_Tags.text_id = {self.id}'
        return db.run_select(query=query)

    def write_to_db(self, user_id: int, con=None) -> None:
        query = f'insert into Texts (title, text_file, release_date, lang, descr, age_restr)\
                values ("{self.title}", "{self.text_file}", "{self.release_date}", \
                        "{self.lang}", "{self.descr}", "{self.age_restr}")'

        self.id = db.modify_table(query=query, con=con)
        query = f'insert into Texts_Users (text_id, user_id, is_author)\
                values ("{self.id}", "{user_id}", "1")'
        db.modify_table(query=query, con=con)


    def delete_from_db(self, con=None) -> None:
        db.modify_table(query=f'delete from Texts where id = "{self.id}"', con=con)

        # junction tables with the same field name
        for table in ['Texts_Users', 'Texts_Tags', 'Texts_Fandoms']:
            db.modify_table(query=f'delete from {table} where text_id="{self.id}"', con=con)

    def __repr__(self) -> str:
        query = f'select Users.username from Texts_Users inner join Users \
                on Texts_Users.user_id = Users.id where Texts_Users.is_author = 1 \
                and Texts_Users.text_id = {self.id}'
        author = db.run_select(query=query)[0][0]
        return f'{self.__class__.__name__}: {self.title} by {author} published {self.release_date}'


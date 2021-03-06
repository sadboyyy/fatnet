class NewsModel:
    def __init__(self, connection):  # connecting to db
        self.connection = connection

    def init_table(self):  # create table if not exists
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS news 
                                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                 title VARCHAR(100),
                                 content VARCHAR(1000),
                                 user_id INTEGER
                                 )''')
        cursor.close()
        self.connection.commit()

    def insert(self, title, content, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO news 
                          (title, content, user_id) 
                          VALUES (?,?,?)''', (title, content, str(
            user_id),))  # when post note, id, title and content
        cursor.close()
        self.connection.commit()

    def get(self, news_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM news WHERE id = ?",
                       (str(news_id),))  # get 1 note using its id
        row = cursor.fetchone()
        return row

    def get_all(self, user_id=None):  # get all news for user
        cursor = self.connection.cursor()
        if user_id:
            cursor.execute("SELECT * FROM news WHERE user_id = ?",
                           (str(user_id),))
        else:
            cursor.execute("SELECT * FROM news")
        rows = cursor.fetchall()
        return rows

    def delete(self, news_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM news WHERE id = ?''',
                       (str(news_id),))  # delete a note by note_id
        cursor.close()
        self.connection.commit()

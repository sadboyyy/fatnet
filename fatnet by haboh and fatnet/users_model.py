class UsersModel:
    def __init__(self, connection):  # connecting to db
        self.connection = connection

    def init_table(self):  # create table if not exists
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             user_name VARCHAR(50),
                             password_hash VARCHAR(128)
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, user_name, password_hash):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users 
                          (user_name, password_hash) 
                          VALUES (?,?)''', (user_name,
                                            password_hash))  # when user being registered only his login and hash needed
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (
            str(user_id)))  # get user login and md5(password) by its id
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")  # get db
        rows = cursor.fetchall()
        return rows

    def exists(self, user_name, password_hash):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE user_name = ? AND password_hash = ?",
            (user_name,
             password_hash))  # checks if a user in db on login/registration
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)

    def exists_only_by_name(self, username):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = ?", (
            username,))  # check if user with username login exists on registration
        row = cursor.fetchone()
        return bool(row)

    def exists_only_by_id(self, userid):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (
            userid,))  # check if user with userid id exists on registration
        row = cursor.fetchone()
        return bool(row)

    def get_hash(self, userid):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?",
                       (userid,))  # get password hash by user id
        row = cursor.fetchone()
        return row[2]

    def get_table_size(self):
        return len(self.get_all())  # get user amount

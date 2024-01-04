import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                chat_id INTEGER,
                today_points INTEGER,
                total_points INTEGER,
                today_requests INTEGER,
                total_requests INTEGER,
                meloman_count INTEGER
            )
        ''')
        self.conn.commit()

    def add_user(self, user):
        self.cursor.execute('''
            INSERT INTO users (name, chat_id, today_points, total_points, today_requests, total_requests, meloman_count)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (user.name, user.chat_id, user.today_points, user.total_points, user.today_requests,
              user.total_requests, user.meloman_count))
        self.conn.commit()
        user.id = self.cursor.lastrowid

    def delete_user(self, user_id):
        self.cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        self.conn.commit()

    def get_all_users(self):
        self.cursor.execute('SELECT * FROM users')
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.cursor.close()
        self.conn.close()

import sqlite3
import threading

class DB:
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.conn.execute("""CREATE TABLE IF NOT EXISTS "users" (
            "username"  TEXT NOT NULL UNIQUE,
            "count"     INTEGER NOT NULL,
            PRIMARY KEY("username")
        );""")
        self.lock = threading.Lock()

    def execute(self, query, *params):
        self.lock.acquire()
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        cursor.close()
        self.conn.commit()
        self.lock.release()
    
    def addUser(self, username):
        query = """INSERT INTO "users" (username, count) VALUES (?, ?)"""
        self.execute(query, username, 0)

    def addCount(self, username, count: int):
        query = """UPDATE users SET count=? WHERE username=?"""
        self.execute(query, count, username)
        
    def search(self, username: str) -> int | None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        records = cursor.fetchall()
        cursor.close()
        return records

    def close(self):
        self.conn.close()

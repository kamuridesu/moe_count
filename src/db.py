import sqlite3


class DB:
    def __init__(self):
        self.locked = False
        self.conn = sqlite3.connect("users.db")
        
        self.conn.execute("""CREATE TABLE IF NOT EXISTS "users" (
            "username"	TEXT NOT NULL UNIQUE,
            "count"	INTEGER NOT NULL,
            PRIMARY KEY("username")
        );""")

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def insert(self, query, *params):
        while self.locked:
            pass
        self.lock()
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        cursor.close()
        self.conn.commit()
        self.unlock()
    
    def addUser(self, username):
        query = """INSERT INTO "users" (username, count) VALUES (?, ?)"""
        self.insert(query, username, 0)

    def addCount(self, username, count: int):
        query = """UPDATE users SET count=? WHERE username=?"""
        self.insert(query, count, username)
        
    def search(self, username: str) -> int | None:
        while self.locked:
            pass
        self.lock()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=\"%s\"" % username)
        records = cursor.fetchall()
        cursor.close()
        self.unlock()
        return records

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = DB()
    db.addUser("kamuridesu")
    for i in range(10):
        actual_cuont = db.search("kamuridesu")
        db.addCount("kamuridesu", actual_cuont + 1)
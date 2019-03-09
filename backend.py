import sqlite3 as db

class Database:

    def __init__(self, dbase):
        self.conn = db.connect(dbase)
        self.cur = self.conn.cursor()
        query = self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        query = self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title, author, year, isbn))
        self.conn.commit()

    def view(self):
        query = self.cur.execute("SELECT * FROM book")
        row  = query.fetchall()
        return row

    def search(self, title="", author="", year="", isbn=""):
        query = self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        row = query.fetchall()
        return row

    def delete(self, id):
        query = self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        query = self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

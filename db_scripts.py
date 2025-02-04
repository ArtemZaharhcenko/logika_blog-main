import sqlite3


class DBManager():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = None
        self.cursor = None

    def open_db(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()

    def get_articles(self):
        self.open_db()
        self.cursor.execute(""" SELECT * FROM articles""")
        data = self.cursor.fetchall()
        self.conn.close()

        return data
    
    def get_categories(self):
        self.open_db()
        self.cursor.execute(""" SELECT * FROM categories""")
        data = self.cursor.fetchall()
        self.conn.close()

        return data
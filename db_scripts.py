import sqlite3

class DataBaseManager:
    def __init__(self, dbname):
        self.conn = None
        self.cursor = None
        self.dbname = dbname

    def open(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def search_item(self, query):
        self.open()
        query = "%" + query + "%"
        self.cursor.execute("""SELECT * FROM items WHERE (title LIKE ? OR content LIKE ?)""", [query, query])
        data = self.cursor.fetchall()
        self.close()
        return data

    def get_all_items(self):
        self.open()
        self.cursor.execute("""SELECT * FROM items""")
        data = self.cursor.fetchall()
        self.close()
        return data

    def get_item(self, item_id):
        self.open()
        self.cursor.execute("""SELECT * FROM items WHERE id=?""", [item_id])
        data = self.cursor.fetchone()
        self.close()
        return data
    
    def get_all_categories(self):
        self.open()
        self.cursor.execute("""SELECT * FROM categories""")
        data = self.cursor.fetchall()
        self.close()
        return data

    def get_category_items(self, category_id):
        self.open()
        self.cursor.execute("""SELECT * FROM items WHERE category_id=?""", [category_id])
        data = self.cursor.fetchall()
        self.close()
        return data

    def get_item(self, item_id):
        self.open()
        self.cursor.execute("""
            SELECT items.*, categories.title AS category_title
            FROM items
            JOIN categories ON items.category_id = categories.id
            WHERE items.id = ?
        """, [item_id])
        data = self.cursor.fetchone()
        self.close()
        return data

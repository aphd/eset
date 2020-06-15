import sqlite3

class Reader_db():
    def __init__(self, db_fn):
        self.connection = sqlite3.connect(db_fn)
        self.cursor = self.connection.cursor()

    def get(self, sql_statement):
        rows = [row for row in self.cursor.execute(sql_statement)]
        columns = next(zip(*self.cursor.description))
        rows.insert(0, columns)
        return rows

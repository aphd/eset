import sqlite3
import re
from app.query import Query


class Writer_db():

    def __init__(self, fn):
        super().__init__()
        self.connection = sqlite3.connect(fn)
        self.cursor = self.connection.cursor()
        self._create_db()

    def _create_db(self):
        q = Query()
        funcs = [func for func in dir(q) if re.search('^create_', func)]
        for func in funcs:
            self.cursor.execute(getattr(q, func)())
        self.connection.commit()

    def insert(self, rows, sql_statement):
        try:
            self.cursor.executemany(sql_statement, rows)
        except sqlite3.IntegrityError as e:
            print('##### sqlite3.IntegrityError ', e)
        self.connection.commit()

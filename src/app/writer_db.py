import sqlite3
from app.query import Query


class Writer_db():

    def __init__(self, fn):
        super().__init__()
        self.connection = sqlite3.connect(fn)
        self.cursor = self.connection.cursor()
        self._create_db()

    def _create_db(self):
        q = Query()
        self.cursor.execute(q.create_tx_tbl())
        self.cursor.execute(q.create_block_tbl())
        self.cursor.execute(q.create_ethGasStation_tbl())
        self.connection.commit()

    def insert(self, rows, sql_statement):
        try:
            self.cursor.executemany(sql_statement, rows)
        except sqlite3.IntegrityError as e:
            print('##### sqlite3.IntegrityError ', e)
        self.connection.commit()

import sqlite3
from query import Query


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

    def insert_tx(self, rows):
        try:
            self.cursor.executemany(
                'INSERT OR IGNORE INTO tx VALUES (?,?,?,?,?,?,?,?)', rows
            )
        except sqlite3.IntegrityError as e:
            print('##### sqlite3.IntegrityError ', e)
        self.connection.commit()
        self.connection.close()


if __name__ == '__main__':
    from fetch_block_tx import Fetch_block_tx
    import glob
    import re

    w = Writer_db('db.sqlite3')
    values = [
        Fetch_block_tx.get_tx(fn)
        for fn in glob.glob('/tmp/output-block_tx_6834287-6840556/*')
        if re.search('\/\d{7}-[a-z0-9]{7}$', fn) and Fetch_block_tx.get_tx(fn)
    ]
    w.insert_tx(values)

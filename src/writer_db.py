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
    import argparse

    parser = argparse.ArgumentParser(description='...')
    parser.add_argument('--dir', required=True, help='txs path (/tmp/txs/)')
    parser.add_argument('--db', required=True, help='db name (db.sqlite3)')
    w = Writer_db(parser.parse_args().db)
    w.insert_tx([
        tx for tx in [
            Fetch_block_tx.get_tx(fn) for fn in glob.glob(parser.parse_args().dir + '*') if re.search('\/\d{7}-[a-z0-9]{7}$', fn)
        ] if tx
    ])

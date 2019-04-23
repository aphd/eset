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


if __name__ == '__main__':
    import glob
    import re
    import argparse
    from app.reader import Reader
    from app.transformer import Transformer

    parser = argparse.ArgumentParser(description='...')
    parser.add_argument('--dir', required=True, help='txs path (/tmp/txs/)')
    parser.add_argument('--db', required=True, help='db name (db.sqlite3)')
    w = Writer_db(parser.parse_args().db)
    r = Reader(parser.parse_args().db)
    w.insert([
        tx for tx in [
            r.get([fn], Transformer().tx_trafo) for fn in glob.glob(parser.parse_args().dir + '*') if re.search('\/\d{7}-[a-z0-9]{7}$', fn)
        ] if tx
    ], 'INSERT OR IGNORE INTO tx VALUES (?,?,?,?,?,?,?,?)')
    w.connection.close()

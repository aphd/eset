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

    # print(r.get('/tmp/output-tx-6896884-6933380/6896885-4e90caf', Transformer().tx_trafo))

    # for fn in glob.glob(parser.parse_args().dir + '*')[0:100]:
    #     if re.search('\/\d{7}-[a-z0-9]{7}$', fn):
    #         print(r.get(fn, Transformer().tx_trafo))

    # print([
    #     tx for tx in [
    #         r.get(fn, Transformer().tx_trafo) for fn in glob.glob(parser.parse_args().dir + '*')[0:10] if re.search('\/\d{7}-[a-z0-9]{7}$', fn)
    #     ] if tx
    # ])

    w.insert_tx([
        tx for tx in [
            r.get(fn, Transformer().tx_trafo) for fn in glob.glob(parser.parse_args().dir + '*') if re.search('\/\d{7}-[a-z0-9]{7}$', fn)
        ] if tx
    ])

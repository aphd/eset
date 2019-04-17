import sqlite3
from query import Query


class Reader():
    # TODO split the class into read_sqlite and read_json
    def __init__(self, db_fn):
        self.connection = sqlite3.connect(db_fn)
        self.cursor = self.connection.cursor()
        self.tx_columns = self._get_tx_columns('select * from tx limit 0')

    def get_txs(self):
        q = Query()
        rows = [row for row in self.cursor.execute(q.get_txs())]
        columns = next(zip(*self.cursor.description))
        rows.insert(0, columns)
        return rows

    def _get_tx_columns(self, query):
        self.cursor.execute(query)
        return next(zip(*self.cursor.description))

    def get_tx_from_file(self, tx_fn):
        from transformer import Transformer
        import json
        t = Transformer()
        try:
            tx = json.loads(open(tx_fn).read())
        except ValueError as e:
            print('ValueError: ', tx_fn)
            return False
        try:
            tx = t._get_tx_transformed(tx)
        except:
            print('_get_tx_transformed exception', tx_fn)
            return False
        return tuple(tx[key] for key in self.tx_columns)


if __name__ == '__main__':
    rd = Reader('db.sqlite3')
    print(rd.get_txs())

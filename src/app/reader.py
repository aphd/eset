import sqlite3
from app.query import Query
import traceback
import json


class Reader():
    # TODO split the class into read_sqlite and read_json, and apply polymorphism
    # TODO add get_block and get_oracle from db (trying to have the same method with get_txs)
    def __init__(self, db_fn):
        self.connection = sqlite3.connect(db_fn)
        self.cursor = self.connection.cursor()

    def get(self, fns, trafo):
        try:
            dct = {}
            for fn in fns:
                dct.update(json.loads(open(fn).read()))
            return tuple(trafo(dct))
        except Exception:
            traceback.print_exc()
        return False

    def get_txs(self):
        q = Query()
        rows = [row for row in self.cursor.execute(q.get_txs())]
        columns = next(zip(*self.cursor.description))
        rows.insert(0, columns)
        return rows


if __name__ == '__main__':
    pass

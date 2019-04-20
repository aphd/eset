import sqlite3
from query import Query
import traceback
import json


class Reader():
    # TODO split the class into read_sqlite and read_json, and apply polymorphism (get_tx from db or json_file)
    def __init__(self, db_fn):
        self.connection = sqlite3.connect(db_fn)
        self.cursor = self.connection.cursor()

    def get(self, fn, trafo):
        try:
            return tuple(trafo(json.loads(open(fn).read())))
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

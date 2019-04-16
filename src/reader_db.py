import sqlite3
from query import Query


class Reader_db():
    def __init__(self, fn):
        super().__init__()
        self.connection = sqlite3.connect(fn)
        self.cursor = self.connection.cursor()

    def read_txs(self):
        q = Query()
        rows = [row for row in self.cursor.execute(q.get_txs())]
        columns = tuple([
            description[0] for description in self.cursor.description
        ])
        rows.insert(0, columns)
        return rows


if __name__ == '__main__':
    rd = Reader_db('db.sqlite3')
    print(rd.read_txs())

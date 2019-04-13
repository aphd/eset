from writer import Writer
import sqlite3
from query import Query


class Writer_db(Writer):

    def __init__(self):
        super().__init__()
        self.connection = sqlite3.connect(self.config['FILE']['db'])
        self.cursor = self.connection.cursor()
        self._create_db()

    def _create_db(self):
        q = Query()
        self.cursor.execute(q.create_tx_tbl())
        self.cursor.execute(q.create_block_tbl())
        self.cursor.execute(q.create_ethGasStation_tbl())
        self.connection.commit()

    def insert_tx(self, values):
        self.cursor.executemany(
            'INSERT INTO tx VALUES (?,?,?,?,?,?,?,?)', values
        )
        self.connection.commit()
        self.connection.close()


if __name__ == '__main__':
    from reader_tx import Reader_tx
    import glob
    w = Writer_db()
    r_tx = Reader_tx()
    values = [r_tx.read_tx(fn) for fn in glob.glob('output-tx/*')]
    w.insert_tx(values)

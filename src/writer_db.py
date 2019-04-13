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

    def insert_tx(self, rows):
        try:
            self.cursor.executemany(
                'INSERT INTO tx VALUES (?,?,?,?,?,?,?,?)', rows
            )
        except sqlite3.IntegrityError as e:
            print(e, rows[0], rows[1])
        self.connection.commit()
        self.connection.close()


if __name__ == '__main__':
    from reader_tx import Reader_tx
    import glob
    w = Writer_db()
    r_tx = Reader_tx()
    values = [r_tx.read_tx(fn) for fn in glob.glob('output-tx/*')]
    w.insert_tx(values)

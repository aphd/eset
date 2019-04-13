from writer import Writer
import sqlite3
from query import Query


class Writer_db(Writer):

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
                'INSERT INTO tx VALUES (?,?,?,?,?,?,?,?)', rows
            )
        except sqlite3.IntegrityError as e:
            print(e, rows[0], rows[1])
        self.connection.commit()
        self.connection.close()


if __name__ == '__main__':
    from reader_tx import Reader_tx
    import configparser
    import glob

    config = configparser.ConfigParser()
    config.read('config.ini')
    w = Writer_db(config['FILE']['db'])
    r_tx = Reader_tx()
    values = [r_tx.read_tx(fn) for fn in glob.glob('output-tx/*')]
    w.insert_tx(values)

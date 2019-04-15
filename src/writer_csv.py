import csv


class Writer_csv():

    def __init__(self):
        super().__init__()

    def write_txs(self, out, txs):
        with open(out, mode='a') as df_file:
            df_writer = csv.writer(
                df_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for tx in txs:
                df_writer.writerow(tx)


if __name__ == '__main__':
    from reader_db import Reader_db
    r_db = Reader_db('db.sqlite3')
    w_csv = Writer_csv()
    w_csv.write_txs('txs.csv', r_db.read_txs())

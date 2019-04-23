class Writer_csv():

    def __init__(self):
        pass

    def write_txs(self, out, txs):
        import csv
        with open(out, mode='w') as df_file:
            df_writer = csv.writer(
                df_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for tx in txs:
                df_writer.writerow(tx)


if __name__ == '__main__':
    from app.reader_db import Reader_db
    from app.query import Query
    r = Reader_db('./db.sqlite3')
    # Writer_csv().write_txs('./txs.csv', r.get(Query().get_txs()))
    Writer_csv().write_txs('./block.csv', r.get(Query().get_blocks()))

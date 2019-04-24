if __name__ == '__main__':
    import glob
    import re
    import argparse
    from app.reader_fn import Reader_fn
    from app.transformer import Transformer
    from app.writer_db import Writer_db

    parser = argparse.ArgumentParser(description='...')
    parser.add_argument('--dir', required=True, help='txs path (/tmp/txs/)')
    parser.add_argument('--db', required=True, help='db name (db.sqlite3)')
    w = Writer_db(parser.parse_args().db)
    r = Reader_fn()

    def insert_tx():
        w.insert([
            tx for tx in [
                r.get([fn], Transformer().tx_trafo) for fn in glob.glob(parser.parse_args().dir + '*') if re.search('\/\d{7}-[a-z0-9]{7}$', fn)
            ] if tx
        ], 'INSERT OR IGNORE INTO tx VALUES (?,?,?,?,?,?,?,?)')

    def insert_block():
        w.insert([
            block for block in [
                r.get((fn, fn + '_lgp'), Transformer().block_trafo) for fn in glob.glob(parser.parse_args().dir + '*') if re.search('\/\d{7}$', fn)
            ] if block
        ], 'INSERT OR IGNORE INTO block VALUES (?,?,?,?,?,?)')

    insert_block()
    w.connection.close()

import glob
import re
import argparse
from argparse import RawTextHelpFormatter
from app.reader_fn import Reader_fn
from app.reader_db import Reader_db
from app.writer_csv import Writer_csv
from app.transformer import Transformer as Trafo
from app.writer_db import Writer_db
from app.query import Query


class Client():

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Client for the Empirical Study of Ethereum Transactions', usage='To write a sqlite file from a list of files:\n $> python app/client.py --src test/fixture/blocks/\* --tgt /tmp/db.sqlite3 --func block2db\n $> sqlite3 /tmp/db.sqlite3 \'select * from block\'\n\nTo write a csv file from a sqlite file:\n $> python app/client.py --src /tmp/db.sqlite3 --tgt /tmp/block.csv --func block2csv',
            formatter_class=RawTextHelpFormatter)
        parser.add_argument('--src', required=True,
                            help='source')
        parser.add_argument('--tgt', required=True,
                            help='target')
        parser.add_argument('--func', required=True,
                            help='Client class method to run')
        args = parser.parse_args()
        self.src = args.src
        self.tgt = args.tgt
        self.func = args.func
        # TODO to avoid  if-else, I should split the client in two parts
        if (re.search('.sqlite3$', self.tgt)):
            self.w = Writer_db(self.tgt)
            self.r = Reader_fn()
        elif (re.search('.csv$', self.tgt)):
            self.w = Writer_csv()
            self.r = Reader_db(self.src)

    def _insert(self, rows, query):
        self.w.insert([row for row in rows if row], query)

    def block2db(self):
        self._insert([
            self.r.get((fn, fn + '_lgp'), Trafo('block').get()) for fn in glob.glob(self.src) if re.search('\/\d{7}$', fn)], 'INSERT OR IGNORE INTO block VALUES (?,?,?,?,?,?)')

    def tx2db(self):
        self._insert([
            self.r.get([fn], Trafo('tx').get()) for fn in glob.glob(self.src) if re.search('\/\d{7}-[a-z0-9]{7}$', fn)], 'INSERT OR IGNORE INTO tx VALUES (?,?,?,?,?,?,?,?)')

    def oracle2db(self):
        self.etherchain2db()
        self.ethGasStation2db()

    def etherchain2db(self):
        rows = [
            self.r.get([fn], Trafo('etherchain').get()) for fn in glob.glob(self.src) if re.search('\/\d{10}_etherchain$', fn)]
        self._insert(
            rows, 'INSERT OR IGNORE INTO etherchain VALUES (?,?,?,?,?)')

    def ethGasStation2db(self):
        rows = [
            self.r.get([fn], Trafo('ethGasStation').get()) for fn in glob.glob(self.src) if re.search('\/\d{10}_ethgasstation$', fn)]
        self._insert(
            rows, 'INSERT OR IGNORE INTO ethGasStation VALUES (?,?,?,?,?,?)')

    def oracle2csv(self):
        self.w.write_txs(self.tgt, self.r.get(Query().get_oracles()))

    def block2csv(self):
        self.w.write_txs(self.tgt, self.r.get(Query().get_blocks()))

    def tx2csv(self):
        self.w.write_txs(self.tgt, self.r.get(Query().get_txs()))


if __name__ == '__main__':
    getattr(Client(),  Client().func)()

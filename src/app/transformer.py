import dateutil.parser
import time
import sqlite3


class Transformer():

    def __init__(self, tbl_name):
        self.connection = sqlite3.connect('./test/fixture/db.sqlite3')
        self.cursor = self.connection.cursor()
        self.columns = self._get_columns(tbl_name)
        self.tbl_name = tbl_name

    def _get_unix_ts(self, date):
        dt = dateutil.parser.parse(date)
        return int(time.mktime(dt.timetuple()))

    def _get_columns(self, tbl):
        sql = tbl.join(['select * from ', ' limit 0'])
        self.cursor.execute(sql)
        return next(zip(*self.cursor.description))

    def _tx(self, tx):
        tx['received'] = self._get_unix_ts(tx['received'])
        tx['confirmed'] = self._get_unix_ts(tx['confirmed'])
        tx['gas_price'] = int(tx['gas_price'] / 1000000000)
        tx['hash'] = tx['hash'][0:6]
        return tuple([tx[key] for key in self._get_columns('tx')])

    def _etherchain(self, oracle):
        return [oracle[key] for key in ['safeLow', 'standard', 'fast', 'fastest']]

    def _ethGasStation(self, oracle):
        return [oracle[key] for key in self.columns]

    def _block(self, block):
        block['lowest_gas_price'] = float(block['lowest_gas_price'])
        block['received_time'] = self._get_unix_ts(block['received_time'])
        block['fees'] = int(block['fees'] / 1000000000)
        return tuple([block[key] for key in self.columns])

    def get(self):
        return getattr(self, '_' + self.tbl_name)

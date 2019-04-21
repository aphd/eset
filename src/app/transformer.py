import dateutil.parser
import time
import sqlite3


class Transformer():

    def __init__(self):
        self.connection = sqlite3.connect('./data/db.sqlite3')
        self.cursor = self.connection.cursor()

    def _get_unix_ts(self, date):
        dt = dateutil.parser.parse(date)
        return int(time.mktime(dt.timetuple()))

    def _get_tx_columns(self, query):
        self.cursor.execute(query)
        return next(zip(*self.cursor.description))

    def tx_trafo(self, tx):
        tx['received'] = self._get_unix_ts(tx['received'])
        tx['confirmed'] = self._get_unix_ts(tx['confirmed'])
        tx['gas_price'] = int(tx['gas_price'] / 1000000000)
        tx['hash'] = tx['hash'][0:6]
        return tuple([tx[key] for key in self._get_tx_columns('select * from tx limit 0')])

    def oracle_ec_trafo(self, oracle):
        return [oracle[key] for key in ['safeLow', 'standard', 'fast', 'fastest']]


if __name__ == '__main__':
    pass

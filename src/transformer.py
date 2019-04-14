import dateutil.parser
import time


class Transformer():

    def _get_unix_ts(self, date):
        dt = dateutil.parser.parse(date)
        return int(time.mktime(dt.timetuple()))

    def _get_tx_transformed(self, tx):
        tx['hash'] = tx['hash'][0:6]
        tx['received'] = self._get_unix_ts(tx['received'])
        tx['confirmed'] = self._get_unix_ts(tx['confirmed'])
        return tx

import json
import time
import dateutil.parser


class Reader_tx:

    def __init__(self):
        pass

    def _get_unix_ts(self, date):
        dt = dateutil.parser.parse(date)
        return int(time.mktime(dt.timetuple()))

    def _get_tx_transformed(self, tx):
        tx['hash'] = tx['hash'][0:6]
        tx['received'] = self._get_unix_ts(tx['received'])
        tx['confirmed'] = self._get_unix_ts(tx['confirmed'])
        return tx

    def read_tx(self, fn):
        # Since hash is truncated to the first 6 characters,considerable space is saved
        tx = json.loads(open(fn).read())
        tx = self._get_tx_transformed(tx)
        # TODO get these fields from the table schema!
        tx_fields = [
            'block_height',
            'hash',
            'gas_price',
            'gas_used',
            'fees',
            'received',
            'confirmed',
            'size'
        ]
        return tuple(tx[key] for key in tx_fields)


if __name__ == '__main__':
    import glob
    r = Reader_tx()
    print([r.read_tx(fn) for fn in glob.glob('output-tx/*')])

from fetch import Fetch
from transformer import Transformer
import re
import os
import json


class Fetch_block_tx(Fetch):

    def __init__(self, block_id=False):
        super().__init__()
        self.block_id = str(block_id)

    def fetch_block(self):
        print(self.config['API']['block'] + self.block_id)
        return self.curl(self.config['API']['block'] + self.block_id, self.block_id)

    def fetch_tx(self, url):
        return self.curl(url, '-'.join([
            self.block_id,
            re.search('.+\/(.+)', url)[1][0:7]
        ]))

    @staticmethod
    def get_tx(fn):
        t = Transformer()
        tx = json.loads(open(fn).read())
        tx = t._get_tx_transformed(tx)
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

    def get_txs(self):
        fn = '/'.join([self.output, self.block_id])
        return json.loads(open(fn).read())['txids']


if __name__ == '__main__':
    def get_next_block_id():
        return int(max(
            re.search('^(\d{7})', val)[0] for val in os.listdir('output-block_tx')
        )) + 1
    while True:
        f = Fetch_block_tx(get_next_block_id())
        f.fetch_block()
        for tx in f.get_txs():
            f.fetch_tx(f.config['API']['tx'] + tx)

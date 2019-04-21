from fetch import Fetch
import re
import os
import json


class Fetch_tx(Fetch):

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

    def get_txs(self, fn):
        try:
            return json.loads(open(fn).read())['txids']
        except:
            print('get_txs exception: ', fn)
            return []


if __name__ == '__main__':
    from fetch_block import Fetch_block

    def get_next_block_id():
        return int(max(
            re.search('^(\d{7})', val)[0] for val in os.listdir('data/output-block')
        )) + 1
    while True:
        block_id = get_next_block_id()
        f = Fetch_tx(block_id)
        f_bck = Fetch_block(block_id)
        f_bck.fetch_block_lowest_gas_price()
        for tx in f.get_txs(f_bck.fetch_block()):
            f.fetch_tx(f.config['API']['tx'] + tx)

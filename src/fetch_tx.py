from fetch import Fetch
from reader import Reader
import re


class Fetch_tx(Fetch):

    def __init__(self):
        super().__init__()

    def download_file(self, url, block_id):
        return self.curl(url, '-'.join([
            str(block_id),
            re.search('.+\/(.+)', url)[1][0:7]
        ]))


if __name__ == '__main__':
    f = Fetch_tx()
    blocks_id = list(range(6819000, 6820000))
    for block_id in blocks_id:
        print(block_id)
        r = Reader()
        txs = r.get_txs_from_block(block_id)
        print(len(txs))
        for tx in txs:
            f.download_file(f.config['API']['tx'] + tx, block_id)

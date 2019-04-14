from fetch import Fetch
from reader import Reader
import re
import os


class Fetch_tx(Fetch):

    def __init__(self):
        super().__init__()

    def download_file(self, url, block_id):
        return self.curl(url, '-'.join([
            str(block_id),
            re.search('.+\/(.+)', url)[1][0:7]
        ]))

    def get_max_id_from_fn(self, dir):
        return int(max(re.search('^(\d{7})', val)[0]
                       for val in os.listdir(dir)))


if __name__ == '__main__':
    import time
    output_tx_dir = 'output-tx'
    start = time.time()
    f = Fetch_tx()
    for i in list(range(8)):
        block_id = f.get_max_id_from_fn(output_tx_dir) + 1
        r = Reader()
        print('#### block_id #### ', block_id)
        txs = r.get_txs_from_block(block_id)
        if len(txs) == 0:
            open(
                '/'.join([output_tx_dir, str(block_id) + '_no_txs']), 'a'
            ).close()
        for tx in txs:
            f.download_file(f.config['API']['tx'] + tx, block_id)
    end = time.time()
    print(end - start)

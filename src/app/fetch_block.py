from fetch import Fetch
import re
import os
import json


class Fetch_block(Fetch):

    def __init__(self, block_id):
        super().__init__()
        self.block_id = max(os.listdir(self.output), default=block_id)

    def fetch_block(self):
        return self.curl(self.config['API']['block'] + self.block_id, self.block_id)

    def fetch_block_lowest_gas_price(self):
        fn = self.curl(
            self.config['API']['block_lowest_gas_price'] + self.block_id, self.block_id + '_lgp')
        fh = open(fn, 'r')
        for line in fh.readlines():
            if 'Lowest Gas Price:' in line:
                try:
                    lgp = re.search(
                        'Lowest Gas Price:</th><td>(\d+(\.\d{1,})?) GWei', line)[1]
                    bt = re.search((' \(Mined in (\d{1,})s\)'), line)[1]
                    fh = open(fn, 'w')
                    json.dump(
                        {'id': self.block_id, 'lowest_gas_price': lgp, 'block_time': bt}, fh)
                except Exception as e:
                    print('Lowest Gas Price Exception:', e, ' fn:', fn)
        fh.close()
        return fn

if __name__ == '__main__':
    fb = Fetch_block(block_id=10000000)
    while True:
        fb.block_id = str(int(fb.block_id) + 1)
        fb.fetch_block()

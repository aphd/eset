from fetch import Fetch
import re
import os
import json


class Fetch_block(Fetch):

    def __init__(self, block_id=False):
        super().__init__()
        self.block_id = str(block_id)

    def fetch_block(self):
        return self.curl(self.config['API']['block'] + self.block_id, self.block_id)

    def fetch_block_lowest_gas_price(self):
        fn = self.curl(
            self.config['API']['block_lowest_gas_price'] + self.block_id, self.block_id + '_lgp')
        lowest_gas_price = open(fn, 'r')
        for line in lowest_gas_price.readlines():
            if 'Lowest Gas Price:' in line:
                try:
                    lgp = re.search(
                        'Lowest Gas Price:</th><td>(\d+(\.\d{1,})?) GWei', line)[1]
                    lowest_gas_price = open(fn, 'w')
                    json.dump(
                        {'id': self.block_id, 'lowest_gas_price': lgp}, lowest_gas_price)
                except Exception as e:
                    print('Lowest Gas Price Exception:', e, ' fn:', fn)
        lowest_gas_price.close()
        return fn


if __name__ == '__main__':
    for block_id in range(7597743, 7601249):
        fb = Fetch_block(block_id)
        fb.fetch_block_lowest_gas_price()
        fb.fetch_block()

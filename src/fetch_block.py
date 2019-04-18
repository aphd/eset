from fetch import Fetch
import re
import os
import json


class Fetch_block(Fetch):

    def __init__(self, block_id=False):
        super().__init__()
        self.block_id = str(block_id)

    def fetch_block(self):
        print(self.config['API']['block'] + self.block_id)
        return self.curl(self.config['API']['block'] + self.block_id, self.block_id)

    def fetch_block_lowest_gas_price(self):
        fn = self.curl(
            self.config['API']['block_lowest_gas_price'] + self.block_id, self.block_id + '_lgp')
        lowest_gas_price = open(fn, 'r')
        for line in lowest_gas_price.readlines():
            if 'Lowest Gas Price:' in line:
                try:
                    lgp = re.search(
                        'Lowest Gas Price:</th><td>([0-9]{1,}) GWei', line)[1]
                    lowest_gas_price = open(fn, 'w')
                    json.dump(
                        {'id': self.block_id, 'lowest_gas_price': int(lgp)}, lowest_gas_price)
                except Exception as e:
                    print('Lowest Gas Price Exception:', e, ' fn:', fn)
        lowest_gas_price.close()
        return fn


if __name__ == '__main__':
    Fetch_block(6545849).fetch_block_lowest_gas_price()

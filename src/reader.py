import configparser
import json
from urllib.request import Request, urlopen


class Reader:

    def __init__(self, block_id=7540130):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.block_id = block_id
        self.hash = '8f39fb4940c084460da00a876a521ef2ba84ad6ea8d2f5628c9f1f8aeb395342'

    def get_block(self):
        return json.loads(self._open_url(self._get_block_api()))

    def get_tx(self):
        return json.loads(self._open_url(self._get_tx_api()))

    def get_txs_from_block(self):
        return self.get_block()['txids']

    def get_gas_price(self):
        return json.loads(self._open_url(self._get_ethgasstation_api()))

    def _get_block_api(self):
        return self.config['API']['block'] + str(self.block_id)

    def _get_ethgasstation_api(self):
        return self.config['API']['ethgasstation']

    def _get_request(self, url):
        return Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    def _get_tx_api(self):
        return self.config['API']['tx'] + str(self.hash)

    def _open_url(self, url):
        return urlopen(self._get_request(url)).read()


if __name__ == '__main__':
    r = Reader()
    r.get_gas_price()

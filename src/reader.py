import configparser
import json
import tokens as cfg
from urllib.request import Request, urlopen
from random import randint


class Reader:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.hash = '8f39fb4940c084460da00a876a521ef2ba84ad6ea8d2f5628c9f1f8aeb395342'

    def get_block(self, block_id):
        # TODO code duplication between fetch and reader
        url = self._get_block_api(block_id) + '?token=' + \
            cfg.tokens[randint(0, len(cfg.tokens) - 1)]
        return json.loads(self._open_url(url))

    def get_tx(self):
        url = self._get_tx_api() + '?token=' + \
            cfg.tokens[randint(0, len(cfg.tokens) - 1)]
        return json.loads(self._open_url(url))

    def get_txs_from_block(self, block_id):
        return self.get_block(block_id)['txids']

    def get_gas_price(self):
        return json.loads(self._open_url(self._get_ethgasstation_api()))

    def _get_block_api(self, block_id):
        return self.config['API']['block'] + str(block_id)

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
    r.get_block(1232132)

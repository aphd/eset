import configparser
import urllib.request
import json


class Reader:

    def __init__(self, block_id=7540130):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.block_id = block_id
        self.hash = '8f39fb4940c084460da00a876a521ef2ba84ad6ea8d2f5628c9f1f8aeb395342'

    def get_block(self):
        with urllib.request.urlopen(self._get_block_api()) as url:
            return json.loads(url.read().decode())

    def get_tx(self):
        with urllib.request.urlopen(self._get_tx_api()) as url:
            return json.loads(url.read().decode())

    def get_txs_from_block(self):
        return self.get_block()['txids']

    def _get_block_api(self):
        return self.config['API']['block'] + str(self.block_id)

    def _get_tx_api(self):
        return self.config['API']['tx'] + str(self.hash)


if __name__ == '__main__':
    r = Reader()
    print(print(r.get_tx()))

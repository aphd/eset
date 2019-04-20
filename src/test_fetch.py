import unittest
from fetch_oracle import Fetch_oracle
from fetch_tx import Fetch_tx
import os


class Test_fetch(unittest.TestCase):

    def setUp(self):
        self.block_id = 6819623
        self.hash = '421a9aa930db114970177ce74c5b519fb4f6e4c5c39327b171edd3fe230bff6b'

    def tearDown(self):
        pass

    def test_download_ethgasstation(self):
        f = Fetch_oracle()
        url = f.config['API']['ethgasstation']
        fn = f.download_fn(url, 'sign')
        ofn = open(fn)
        json = ofn.read()
        ofn.close()
        self.assertTrue(os.path.exists(fn))
        self.assertTrue('fast' in json)
        self.assertTrue('fastest' in json)
        os.remove(fn)

    def test_download_tx(self):
        f = Fetch_tx(self.block_id)
        url = f.config['API']['tx'] + self.hash
        fn = f.fetch_tx(url)
        ofn = open(fn)
        json = ofn.read()
        ofn.close()
        self.assertTrue(os.path.exists(fn))
        self.assertTrue('confirmed' in json)
        self.assertTrue('gas_price' in json)
        os.remove(fn)


if __name__ == '__main__':
    unittest.main()

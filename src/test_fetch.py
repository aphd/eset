import unittest
from fetch_ethgasstation import Fetch_ethgasstation
from fetch_tx import Fetch_tx
import os


class Test_fetch(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_download_ethgasstation(self):
        f = Fetch_ethgasstation()
        url = f.config['API']['ethgasstation']
        fn = f.download_file(url)
        ofn = open(fn)
        json = ofn.read()
        ofn.close()
        self.assertTrue(os.path.exists(fn))
        self.assertTrue('fast' in json)
        self.assertTrue('fastest' in json)
        os.remove(fn)

    def test_download_tx(self):
        f = Fetch_tx()
        url = f.config['API']['tx'] + \
            'da1e94c9d07b263da3916599e151f1c48afb0736a82748bc6699c80f08391fe6'
        fn = f.download_file(url, 12323)
        ofn = open(fn)
        json = ofn.read()
        ofn.close()
        self.assertTrue(os.path.exists(fn))
        self.assertTrue('confirmed' in json)
        self.assertTrue('gas_price' in json)
        os.remove(fn)

    def test_get_max_id_from_fn(self):
        # TODO
        pass


if __name__ == '__main__':
    unittest.main()

import unittest
from fetch_ethgasstation import Fetch_ethgasstation
import os


class Test_fetch_ethgasstation(unittest.TestCase):

    def setUp(self):
        self.f = Fetch_ethgasstation()
        self.url = self.f.config['API']['ethgasstation']

    def tearDown(self):
        os.remove(self.fn)

    def test_download_file(self):
        self.fn = self.f.download_file(self.url)
        self.assertTrue(os.path.exists(self.fn))
        self.assertTrue('fast' and 'fastest' in open(self.fn).read())


if __name__ == '__main__':
    unittest.main()

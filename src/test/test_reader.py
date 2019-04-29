import unittest
from app.reader_fn import Reader_fn
from app.transformer import Transformer as Trafo


class Test_reader(unittest.TestCase):

    def setUp(self):
        self.r_fn = Reader_fn()

    def tearDown(self):
        pass

    def test_get(self):
        get = self.r_fn.get
        assertIsInstance = self.assertIsInstance
        assertFalse = self.assertFalse
        dir = './test/fixture/'
        assertIsInstance(get([dir + 'tx_ok'], Trafo('tx').get()), tuple)
        assertIsInstance(
            get([dir + 'oracle_ec'], Trafo('etherchain').get()), tuple)
        assertIsInstance(get([dir + 'bk', dir + 'bkl'],
                             Trafo('block').get()), tuple)


if __name__ == '__main__':
    unittest.main()

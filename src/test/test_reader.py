import unittest
from app.reader import Reader
from app.transformer import Transformer


class Test_reader(unittest.TestCase):

    def setUp(self):
        self.r = Reader('./test/fixture/db.sqlite3')

    def tearDown(self):
        pass

    def test_get(self):
        get = self.r.get
        assertIsInstance = self.assertIsInstance
        dir = './test/fixture/'
        t = Transformer()
        assertIsInstance(get([dir + 'tx_ok'], t.tx_trafo), tuple)
        assertIsInstance(get([dir + 'oracle_ec'], t.oracle_ec_trafo), tuple)
        assertIsInstance(get([dir + 'bk', dir + 'bkl'], t.block_trafo), tuple)
        self.assertFalse(get([dir + 'tx_err'], t.tx_trafo))


if __name__ == '__main__':
    unittest.main()

import unittest
from app.reader_fn import Reader_fn
from app.transformer import Transformer


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
        t = Transformer()
        assertIsInstance(get([dir + 'tx_ok'], t.tx_trafo), tuple)
        assertIsInstance(get([dir + 'oracle_ec'], t.oracle_ec_trafo), tuple)
        assertIsInstance(get([dir + 'bk', dir + 'bkl'], t.block_trafo), tuple)
        assertFalse(get([dir + 'tx_err'], t.tx_trafo))
        assertFalse(get([dir + 'bk', dir + 'bk_ko'], t.block_trafo), tuple)


if __name__ == '__main__':
    unittest.main()

import unittest
from app.reader import Reader


class Test_reader(unittest.TestCase):

    def setUp(self):
        from app.transformer import Transformer
        self.t = Transformer()
        self.r = Reader('./data/db.sqlite3')
        self.dir = './test/fixture/'

    def tearDown(self):
        pass

    def test_get_tx(self):
        trafo = self.t.tx_trafo
        self.assertIsInstance(self.r.get(self.dir + 'tx_ok', trafo), tuple)
        self.assertFalse(self.r.get(self.dir + 'tx_err', trafo))
        self.assertFalse(self.r.get('', trafo))

    def test_get_oracle_ec(self):
        trafo = self.t.oracle_ec_trafo
        self.assertIsInstance(self.r.get(self.dir + 'oracle_ec', trafo), tuple)


if __name__ == '__main__':
    unittest.main()

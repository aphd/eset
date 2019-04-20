import unittest
from reader import Reader


class Test_reader(unittest.TestCase):

    def setUp(self):
        from transformer import Transformer
        self.t = Transformer()
        self.r = Reader('db.sqlite3')

    def tearDown(self):
        pass

    def test_get_tx(self):
        trafo = self.t.tx_trafo
        self.assertIsInstance(self.r.get('fixture/tx_ok', trafo), tuple)
        self.assertFalse(self.r.get('fixture/tx_err', trafo))
        self.assertFalse(self.r.get('', trafo))

    def test_get_oracle_ec(self):
        trafo = self.t.oracle_ec_trafo
        self.assertIsInstance(self.r.get('fixture/oracle_ec', trafo), tuple)


if __name__ == '__main__':
    unittest.main()

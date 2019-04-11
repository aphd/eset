import unittest
from reader import Reader


class TestReader(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestReader, self).__init__(*args, **kwargs)
        self.r = Reader()

    def test_get_block(self):
        block = self.r.get_block()
        self.assertIsInstance(block, dict)
        self.assertTrue('height' and 'fees' and 'txids' in block)

    def test_get_txs_from_block(self):
        self.assertIsInstance(self.r.get_txs_from_block(), list)

    def test_get_tx(self):
        tx = self.r.get_tx()
        self.assertIsInstance(tx, dict)
        self.assertTrue('gas_limit' and 'gas_used' and 'gas_price' in tx)

    def test_get_gas_price(self):
        gas_price = self.r.get_gas_price()
        self.assertIsInstance(gas_price, dict)
        self.assertTrue('fast' and 'safeLow' and 'average' in gas_price)


if __name__ == '__main__':
    unittest.main()

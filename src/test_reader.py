import unittest
from reader import Reader


class TestReader(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestReader, self).__init__(*args, **kwargs)
        self.r = Reader()

    def test_get_block(self):
        self.assertIsInstance(self.r.get_block(), dict)

    def test_get_txs_from_block(self):
        self.assertIsInstance(self.r.get_txs_from_block(), list)

    def test_get_tx(self):
        self.assertIsInstance(self.r.get_tx(), dict)


if __name__ == '__main__':
    unittest.main()

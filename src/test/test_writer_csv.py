import unittest
import uuid
from app.writer_csv import Writer_csv
import os


class Test_writer_csv(unittest.TestCase):

    def setUp(self):
        self.w = Writer_csv()

    def tearDown(self):
        pass

    def test_write_txs(self):
        fn = '/'.join(['/tmp', str(uuid.uuid4())])
        self.w.write_txs(fn, [(6819000, '0fbeb1', -252, 50, 52776, 150000)])
        ofn = open(fn)
        self.assertTrue('6819000,0fbeb1,-252,50,52776,150000' in ofn.read())
        ofn.close()
        os.remove(fn)


if __name__ == '__main__':
    unittest.main()

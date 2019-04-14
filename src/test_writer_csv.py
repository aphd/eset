import unittest
import uuid
from writer_csv import Writer_csv
import os


class Test_writer_csv(unittest.TestCase):

    def setUp(self):
        self.w = Writer_csv()

    def tearDown(self):
        pass

    def test_write_tx(self):
        fn = '/'.join(['/tmp', str(uuid.uuid4())])
        self.w.write_tx(fn, {
            'block_height': 1564040,
            'received': '2016-05-22T12:43:00Z'
        })
        ofn = open(fn)
        self.assertTrue('1564040,2016-05-22T12:43:00Z' in ofn.read())
        ofn.close()
        os.remove(fn)


if __name__ == '__main__':
    unittest.main()

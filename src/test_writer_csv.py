import unittest
import uuid
from io import StringIO
from writer_csv import Writer_csv


class Test_writer_csv(unittest.TestCase):

    def setUp(self):
        self.w = Writer_csv()

    def tearDown(self):
        pass

    def test_write_tx(self):
        outfile = '/'.join(['/tmp', str(uuid.uuid4())])
        self.w.write_tx(outfile, {
            'block_height': 1564040,
            'received': '2016-05-22T12:43:00Z'
        })
        self.assertTrue('1564040,2016-05-22T12:43:00Z' in open(outfile).read())


if __name__ == '__main__':
    unittest.main()

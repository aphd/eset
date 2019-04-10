import unittest
import uuid
from io import StringIO
from writer import Writer


class TestWriter(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestWriter, self).__init__(*args, **kwargs)
        self.w = Writer()

    def test_write_tx(self):
        outfile = '/'.join(['/tmp', str(uuid.uuid4())])
        tx = ','.join([str(key) for key in self.w._get_tx_transformer()])
        self.w.write_tx(outfile)
        self.assertTrue(tx in open(outfile).read())


if __name__ == '__main__':
    unittest.main()

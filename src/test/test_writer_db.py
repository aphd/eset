import os
import unittest
import uuid
import sqlite3
from app.writer_db import Writer_db


class Test_writer_db(unittest.TestCase):

    def setUp(self):
        self.outfile = '/'.join(['/tmp', str(uuid.uuid4())])
        self.w = Writer_db(self.outfile)

    def tearDown(self):
        self.w.connection.close()
        os.remove(self.outfile)

    def test__create_db(self):
        self.assertIsInstance(self.w.connection, sqlite3.Connection)
        self.assertIsInstance(self.w.cursor, sqlite3.Cursor)
        self.w.cursor.execute(
            'SELECT hash from tx'
        )
        self.w.cursor.execute(
            'SELECT height from block'
        )
        self.w.cursor.execute(
            'SELECT fast from ethGasStation'
        )


if __name__ == '__main__':
    unittest.main()

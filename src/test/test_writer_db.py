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

    def test_insert(self):
        self.w.insert([(0, '12sasx3', 1, 2, 3, 0, 0, 4)],
                      'INSERT OR IGNORE INTO tx VALUES (?,?,?,?,?,?,?,?)')
        self.w.insert([(1, 2, 3, 4, 5, 6)],
                      'INSERT OR IGNORE INTO block VALUES (?,?,?,?,?,?)')


if __name__ == '__main__':
    unittest.main()

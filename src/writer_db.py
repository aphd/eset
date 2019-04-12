from writer import Writer
import sqlite3


class Writer_db(Writer):

    def __init__(self):
        super().__init__()
        self.db = self.config['FILE']['db']
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()

    def _create_db(self):
        # TODO Only first table in create table statement being created
        # https://stackoverflow.com/questions/2928184/only-first-table-in-create-table-statement-being-created?rq=1
        self.cursor.execute(
            open(self.config['FILE']['db_create_table'], 'r').read()
        )
        self.connection.commit()
        self.connection.close()


if __name__ == '__main__':
    w = Writer_db()
    print(w._create_db())

class Query:

    def __init__(self):
        pass

    def create_ethGasStation_tbl(self):
        return '''
            CREATE TABLE IF NOT EXISTS ethGasStation
            (
                fastest INTEGER,
                fast INTEGER,
                safeLow INTEGER,
                average INTEGER,
                block_time REAL,
                blockNum INTEGER
            )
        '''

    def create_tx_tbl(self):
        return '''
            CREATE TABLE IF NOT EXISTS tx
            (
                block_height INTEGER,
                hash TEXT,
                gas_price INTEGER,
                gas_used INTEGER,
                fees INTEGER,
                received INTEGER,
                confirmed INTEGER,
                size INTEGER,
                PRIMARY KEY (block_height, hash)
            )
        '''

    def create_block_tbl(self):
        return '''
            CREATE TABLE IF NOT EXISTS block
            (
                height INTEGER,
                fees INTEGER,
                time INTEGER,
                size INTEGER
            )
        '''

    def get_txs(self):
        return '''
            SELECT
                block_height, hash, received, 
                confirmed, gas_price, gas_used, fees 
            FROM
                tx
        '''


if __name__ == '__main__':
    pass

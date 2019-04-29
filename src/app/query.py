class Query:

    def __init__(self):
        pass

    def create_ethGasStation_tbl(self):
        return '''
            CREATE TABLE IF NOT EXISTS ethGasStation
            (
                timestamp INTEGER,
                fastest INTEGER,
                fast INTEGER,
                safeLow INTEGER,
                average INTEGER,
                blockNum INTEGER,
                PRIMARY KEY (timestamp)
            )
        '''

    def create_etherchain_tbl(self):
        return '''
            CREATE TABLE IF NOT EXISTS etherchain
            (
                timestamp INTEGER,
                safeLow INTEGER,
                standard INTEGER,
                fast INTEGER,
                fastest INTEGER,
                PRIMARY KEY (timestamp)
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
                gas_limit INTEGER,
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
                received_time INTEGER,
                height INTEGER,
                fees INTEGER,
                size INTEGER,
                n_tx INTEGER,
                lowest_gas_price REAL,
                PRIMARY KEY (height)
            )
        '''

    def get_txs(self):
        return '''
            SELECT
                block_height, hash, confirmed - received as waiting_time, gas_price, gas_used , gas_limit, size
            FROM
                tx
            ORDER BY block_height
        '''

    def get_blocks(self):
        return '''
            SELECT
                received_time, height, fees, size, n_tx, lowest_gas_price
            FROM
                block
            ORDER BY height
        '''

    def get_oracles(self):
        return '''
            SELECT
                    o1.timestamp, blockNum, o1.fastest as egs, o2.fastest as ec, lowest_gas_price
            FROM
                    ethgasstation as o1, etherchain as o2, block
            WHERE
                    o1.timestamp BETWEEN o2.timestamp -1 AND o2.timestamp +1
                AND
                    block.height = blockNum
            ORDER BY o1.timestamp
        '''

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
                block_time INTEGER,
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
                height , received_time, fees, size, n_tx, lowest_gas_price,
                received_time - LAG ( received_time, 1, 0 ) OVER ( ORDER BY height ) block_time 
            FROM
                block 
            OFFSET 1;
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

    def get_egs_oracle(self):
        return '''
            select * from ethGasStation order by timestamp
        '''

    def get_received_time_and_delta_from_block(self, height):
        return '''
            select %d, received_time, block_time from block where height = %d;
        ''' % (height, height)

    def get_block_count(self, start_time, end_time):
        return ''' 
            SELECT 
                count(), gas_price, (confirmed-received)/15 
            FROM 
                tx 
            WHERE 
                received > %d and received < %d  group by gas_price order by gas_price;
        ''' % (start_time, end_time)

import json


class Reader_tx:

    def __init__(self):
        pass

    def read_tx(self, fn):
        json_obj = json.loads(open(fn).read())
        tx_fields = [
            'block_height',
            'hash',
            'gas_price',
            'gas_used',
            'fees',
            'received',
            'confirmed',
            'size'
        ]
        # TODO transform received and confirmed in unix_timestamp
        return tuple(json_obj[key] for key in tx_fields)


if __name__ == '__main__':
    import glob
    r = Reader_tx()
    print([r.read_tx(fn) for fn in glob.glob('output-tx/*')])

import csv
from writer import Writer


class Writer_csv(Writer):

    def __init__(self):
        super().__init__()
        self.df = self.config['FILE']['df']

    def _get_tx_transformer(self, tx):
        tx_transformer = ['block_height', 'received']
        return [tx[key] for key in tx_transformer]

    def write_tx(self, out, tx):
        with open(out, mode='a') as df_file:
            df_writer = csv.writer(
                df_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            df_writer.writerow(self._get_tx_transformer(tx))


if __name__ == '__main__':
    from reader import Reader
    r = Reader()
    w = Writer_csv()
    print(r.get_tx())
    print(w.write_tx(w.config['FILE']['df'], r.get_tx()))

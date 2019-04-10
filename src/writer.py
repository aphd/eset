import configparser
import csv
from reader import Reader


class Writer:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.df = self.config['FILE']['df']
        self.r = Reader()

    def _get_tx_transformer(self):
        # TODO implement a transformer
        tx = self.r.get_tx()
        tx_transformer = ['block_height', 'received']
        return [tx[key] for key in tx_transformer]

    def write_tx(self, out):
        with open(out, mode='a') as df_file:
            df_writer = csv.writer(
                df_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            df_writer.writerow(self._get_tx_transformer())

            print(type(df_writer))


if __name__ == '__main__':
    w = Writer()
    print(w.write_tx(w.df))

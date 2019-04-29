class Writer_csv():

    def __init__(self):
        pass

    def write_txs(self, out, txs):
        import csv
        with open(out, mode='w') as df_file:
            df_writer = csv.writer(
                df_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for tx in txs:
                df_writer.writerow(tx)

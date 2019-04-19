from fetch import Fetch
import time


class Fetch_oracle(Fetch):

    def __init__(self):
        super().__init__()
        # TODO get the oracle info from config.ini
        self.oracles = ['ethgasstation', 'etherchain']

    def download_fn(self, url, file_signature):
        # TODO get the oracle info from config.ini
        return self.curl(url, '_'.join([str(int(time.time())), file_signature]))


if __name__ == '__main__':

    from threading import Timer

    f = Fetch_oracle()
    number_of_times_each_minute = 4
    interval = 60 / (number_of_times_each_minute)
    for i in range(number_of_times_each_minute):
        for oracle in f.oracles:
            print(oracle)
            Timer(i * interval, f.download_fn,
                  [f.config['API'][oracle], oracle]).start()

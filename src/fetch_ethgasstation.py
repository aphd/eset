from fetch import Fetch
import time


class Fetch_ethgasstation(Fetch):

    def __init__(self):
        super().__init__()

    def download_file(self, url):
        return self.curl(url, str(int(time.time())))


if __name__ == '__main__':

    from threading import Timer

    f = Fetch_ethgasstation()
    url = f.config['API']['ethgasstation']
    number_of_times_each_minute = 4
    interval = 60 / (number_of_times_each_minute)
    for i in range(number_of_times_each_minute):
        Timer(i * interval, f.download_file, [url]).start()

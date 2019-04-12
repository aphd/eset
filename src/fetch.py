from random import randint
from threading import Timer
import configparser
import subprocess
import time


class Fetch:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def download_file(self, url):
        file_name = self._get_name_from_url(url)
        subprocess.call([
            'curl', url, '-H',
            '.'.join([str(randint(0, 255)) for x in range(4)]),
            '-o', f.config['FILE']['out_dir'] + file_name
        ])

    def _get_name_from_url(self, url):
        # TODO return the file name from the url
        return '-'.join(['ethgasstation', str(int(time.time()))])


if __name__ == '__main__':
    f = Fetch()
    url = f.config['API']['ethgasstation']
    number_of_times_each_minute = 4
    interval = 60 / (number_of_times_each_minute)
    for i in range(number_of_times_each_minute):
        Timer(i * interval, f.download_file, [url]).start()

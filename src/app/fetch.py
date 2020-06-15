import configparser
import subprocess
from random import randint
import app.tokens as cfg
import os


class Fetch:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('./app/config.ini')
        self.output = '/'.join([
            self.config['OUTPUT']['data'], 
            self.__class__.__name__.replace('Fetch_', '')
        ])
        if not os.path.exists(self.output):
            os.makedirs(self.output)

    def curl(self, url, file_signature):
        file_name = self._get_name_from_url(url, file_signature)
        url = url + self._get_random_token()
        subprocess.call([
            'curl', '-s', url, '-H',
            'X-Forwarded-For: ' +
            '.'.join([str(randint(0, 255)) for x in range(4)]),
            '-o', file_name
        ])
        return file_name

    def _get_name_from_url(self, url, file_signature):
        return '/'.join([
            self.output,
            file_signature
        ])

    def _get_random_token(self):
        return '?token=' + cfg.tokens[randint(0, len(cfg.tokens) - 1)]

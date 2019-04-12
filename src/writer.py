import configparser


class Writer:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')


if __name__ == '__main__':
    pass

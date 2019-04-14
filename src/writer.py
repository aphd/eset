import configparser


class Writer:

    def __init__(self):
        # TODO the class writer does not need to depend on config.ini
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')


if __name__ == '__main__':
    pass

import sys
import logging
from datetime import datetime
class Logger(object):
    # creating time stamp
    exact_time = datetime.date(datetime.now())
    def __init__(self, filename=f'logs/{exact_time}.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger(stream=sys.stdout)

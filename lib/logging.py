# LOGGING

# imports
import sys
import logging
from datetime import datetime
class Logger(object):
    # creating time stamp
    exact_time = datetime.date(datetime.now())

    # creating object
    def __init__(self, filename=f'logs/{exact_time}.txt', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a')

    # writing to files every printout
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    # handling error exception
    def flush(self):
        pass

# catching every line from console
sys.stdout = Logger(stream=sys.stdout)

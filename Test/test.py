#python3
import sys
sys.path.append("..")

from datetime import date

today = date.today()

import logging
logging.basicConfig(filename='../logs/' + str(today) + '.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)
logging.info("This is an info log entry")

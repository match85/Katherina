#python3
import os
import platform
import subprocess
import time
import sys

from Test import botoTest

sys.path.append("..")

from config_data import init_config
from utils import deviceHandler
from utils import databaseHandler
from utils import monitor
from datetime import date

today = date.today()

import logging
logging.basicConfig(filename='../logs/' + str(today) + '.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)
logging.info("This is an info log entry")

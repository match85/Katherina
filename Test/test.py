#python3
import sys
sys.path.append("..")

from datetime import date

today = date.today()
import time
from utils import deviceHandler

import logging

print(deviceHandler.getPlugName(1))
#python3
import sys
sys.path.append("..")

from datetime import date

today = date.today()
import time
from utils import deviceHandler
from utils import routinesHandler
import logging

print(routinesHandler.isEnabled("Temperature"))
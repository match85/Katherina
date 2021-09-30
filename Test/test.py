#python3
import sys
sys.path.append("..")
import time
from config_data import deviceInfo
from utils import deviceHandler

deviceInfo.setPhilipsData("motion", 1, "last", time.time())
print(time.time())
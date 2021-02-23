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

#botoTest.update_data("Humidity", 1, "min_hum", 40)

#databaseHandler.setMaxTemperature(1, 22)

#botoTest.put_data2("Humidity", 1, "max_hum", 60)
print(init_config.getDynamoUrl())
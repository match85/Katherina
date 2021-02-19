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

botoTest.update_data("Humidity", 1, "50")
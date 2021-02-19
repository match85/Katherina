#python3
import os
import platform
import subprocess
import time
import sys
sys.path.append("..")

from config_data import init_config
from utils import deviceHandler

print(deviceHandler.getPhoneState(2))
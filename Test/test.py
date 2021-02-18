#python3
import os
import platform
import subprocess
import time

from config_data import init_config
from utils import deviceHandler

print(deviceHandler.getPhoneState(1))
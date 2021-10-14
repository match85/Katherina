#python3
import sys
sys.path.append("..")
import time
from config_data import deviceInfo
from utils import deviceHandler
from alexa_client import AlexaClient

print(deviceHandler.getPlugState(1))
#python3
import json
import platform
import subprocess
import time

from config_data import routineConfig
import requests
from datetime import date
today = date.today()
import logging
logging.basicConfig(filename='../logs/' + str(today) + '.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.INFO)

from utils.pyS150 import MotionSensor
from utils.pyW215 import SmartPlug, ON, OFF
from utils import databaseHandler

def isEnabled(routine):
    return routineConfig.getEnabledState(routine)

def setEnabled(routine, state):
    return routineConfig.setEnabledState(routine, state)
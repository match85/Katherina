#python3
import logging
import sys
import json
import requests

sys.path.append("..")
import time
import datetime
from config_data import deviceInfo
from utils import deviceHandler
from utils import routineHandler
from config_data import routineInfo
from alexa_client import AlexaClient
from utils import statusHandler
from miio import ViomiVacuum
import paho.mqtt.client as mqtt
import socket
import os
from wakeonlan import send_magic_packet
from yeelight import Bulb

''''
from utils.pyW215 import SmartPlug, ON, OFF
sp = SmartPlug(deviceInfo.getDlinkData("plug", 1, "ip"), deviceInfo.getDlinkData("plug", 1, "auth"))
while True:
    print("Total: " + str(sp.total_consumption) + " Current: " + str(sp.current_consumption))
    time.sleep(10)
#send_magic_packet('24.a2.e1.f3.68.2a', ip_address='192.168.1.178', port=80)
'''

bulb_bath = Bulb("192.168.1.161")
deviceHandler.setLightState(3, False)
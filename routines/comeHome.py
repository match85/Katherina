# python3
import sys

sys.path.append("..")
from utils import statusHandler
from utils import deviceHandler
import datetime
import time
import logging

currentTime = datetime.datetime.now().hour
lastSeen = statusHandler.getPhoneLast()
while (not statusHandler.getPhoneState()) and ((currentTime >= 17) or (currentTime <= 5)):
    #logging.info("Coming home investigation started")
    time.sleep(10)
    # deviceHandler.getPhoneState(0)
    if ((lastSeen + 1800) < time.time()) and statusHandler.getPhoneState():
        logging.info("User came home detected")
        deviceHandler.setLightState(3, 'on')

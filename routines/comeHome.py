# python3
import sys

sys.path.append("..")
from utils import statusHandler
from utils import deviceHandler
import datetime
import time

currentTime = datetime.datetime.now().hour
lastSeen = statusHandler.getPhoneLast()
while (not statusHandler.getPhoneState()) and ((currentTime >= 17) or (currentTime <= 5)):
    time.sleep(10)
    # deviceHandler.getPhoneState(0)
    if (statusHandler.getPhoneState() + 1800) < time.time():
        deviceHandler.setLightState(3, 'on')

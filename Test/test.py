#python3
import sys
sys.path.append("..")

from datetime import date

today = date.today()
import time
from utils import deviceHandler

import logging
last = deviceHandler.getMotionState()


now = deviceHandler.getMotionState()
if now > last:
	logging.info("Motion detected on DLink")
	deviceHandler.setLightState(4, "on")
	last = now
if (time.time() > last + 60) and (deviceHandler.getLightState(4)):
	logging.info("No motion detected on DLink for 1 minute")
	deviceHandler.setLightState(4, "off")


if deviceHandler.getLightState(4):
    print("ON")
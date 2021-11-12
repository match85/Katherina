#python3
import sys
sys.path.append("..")
from utils import deviceHandler
import time
import logging

try:
	last = deviceHandler.getMotionState()
except:
	last = 1
now = 0
while True:
	try:
		now = deviceHandler.getMotionState()
	except:
		pass
	if now > last:
		logging.info("Motion detected on DLink")
		deviceHandler.setLightState(4, True)
		last = now
	if (time.time() > last + 60) and (deviceHandler.getLightState(4)):
		logging.info("No motion detected on DLink for 1 minute")
		deviceHandler.setLightState(4, False)

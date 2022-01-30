import sys
sys.path.append("..")
from utils import deviceHandler
from utils import statusHandler
import logging
import time

timeout = int(time.time() - statusHandler.getPhoneLast())
if not statusHandler.getPhoneState():
	logging.info("Left home routine triggered")
	#deviceHandler.alexaSay("Initiating left home routine")
	deviceHandler.setLightState(1, False)
	deviceHandler.setLightState(2, False)
	deviceHandler.setLightState(3, False)
	deviceHandler.setLightState(4, False)
	deviceHandler.setPlugState(0, "off")

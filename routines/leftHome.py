import sys
sys.path.append("..")
from utils import deviceHandler
import logging

if not deviceHandler.getPhoneState(5):
	logging.info("Left home routine triggered")
	deviceHandler.setLightState(1, "off")
	deviceHandler.setLightState(2, "off")
	deviceHandler.setLightState(3, "off")
	deviceHandler.setLightState(4, "off")
	deviceHandler.setPlugState(0, "off")

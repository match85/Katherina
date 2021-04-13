#python3
import sys
sys.path.append("..")
from utils import databaseHandler
from utils import deviceHandler
from utils import routineHandler
import logging

if routineHandler.isEnabled("temp"):
	min = databaseHandler.getMinTemperature(1)
	max = databaseHandler.getMaxTemperature(1)
	print(min)
	print(max)
	r = deviceHandler.getPhoneState(0)
	if not r:
		deviceHandler.setPlugState(0, "off")
	else:
		value = databaseHandler.getCurrentTemperature(1)
		print(value)
		if value <= min:
			logging.info("Low temperature detected")
			deviceHandler.setPlugState(0, "on")
		if value >= max:
			logging.info("High temperature detected")
			deviceHandler.setPlugState(0, "off")
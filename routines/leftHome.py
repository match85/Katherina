import sys
sys.path.append("..")
from utils import deviceHandler
from utils import statusHandler
from config_data import routineInfo
import logging
import time

timeout = int(time.time() - statusHandler.getPhoneLast())

if (not statusHandler.getPhoneState()) and ((routineInfo.getRoutineData("leftHome", "timeout") * 60) <= timeout):
	logging.info("Left home routine triggered")
	deviceHandler.setLightState(1, "off")
	deviceHandler.setLightState(2, "off")
	deviceHandler.setLightState(3, "off")
	deviceHandler.setLightState(4, "off")
	deviceHandler.setPlugState(0, "off")

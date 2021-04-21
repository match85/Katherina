import sys
sys.path.append("..")
from utils import deviceHandler
from config_data import routineInfo
import logging

if not deviceHandler.getPhoneState(int(routineInfo.getRoutineData("leftHome", "timeout"))):
	logging.info("Left home routine triggered")
	deviceHandler.setLightState(1, "off")
	deviceHandler.setLightState(2, "off")
	deviceHandler.setLightState(3, "off")
	deviceHandler.setLightState(4, "off")
	deviceHandler.setPlugState(0, "off")

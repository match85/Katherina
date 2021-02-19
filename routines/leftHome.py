import sys
sys.path.append("..")
from utils import deviceHandler


if not deviceHandler.getPhoneState(5):
	deviceHandler.setLightState(1, "off")
	deviceHandler.setLightState(2, "off")
	deviceHandler.setLightState(3, "off")
	deviceHandler.setLightState(4, "off")
	deviceHandler.setPlugState(0, "off")

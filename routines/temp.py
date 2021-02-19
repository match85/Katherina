#python3
import sys
sys.path.append("..")
from utils import databaseHandler
from utils import deviceHandler

min = databaseHandler.getMinTemperature(1)
max = databaseHandler.getMaxTemperature(1)
r = deviceHandler.getPhoneState(0)
if not r:
	deviceHandler.setPlugState(0, "off")
else:
	value = databaseHandler.getCurrentTemperature(1)
	if value <= min:
		deviceHandler.setPlugState(0, "on")
	if value >= max:
		deviceHandler.setPlugState(0, "off")
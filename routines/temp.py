# python3
import sys

sys.path.append("..")
from utils import deviceHandler
from utils import routineHandler
from utils import statusHandler
import logging

if routineHandler.isEnabled("temp"):
    min = deviceHandler.getMinTemperature()
    max = deviceHandler.getMaxTemperature()
    print(min)
    print(max)
    r = statusHandler.getPhoneState()
    if not r:
        deviceHandler.setPlugState(0, "off")
    else:
        value = statusHandler.getCurrentTemp(1)
        print(value)
        if statusHandler.getDoorState(1) and value <= min:
            if value <= min:
                logging.info("Low temperature detected")
                deviceHandler.setPlugState(0, "on")
        else:
            if value <= min:
                logging.info("Low temperature but door not closed.")
                deviceHandler.setPlugState(0, "off")
        if value >= max:
            logging.info("High temperature detected")
            deviceHandler.setPlugState(0, "off")

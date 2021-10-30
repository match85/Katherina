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
    logging.info("Temperature checking started")
    r = statusHandler.getPhoneState()
    if not r:
        logging.info("No phone detected by temperature routine")
        deviceHandler.setPlugState(0, "off")
    else:
        value = statusHandler.getCurrentTemp(1)
        print(value)
        logging.info("Current temperature: " + value)
        if statusHandler.getDoorState(1):
            if value <= min:
                logging.info("Low temperature detected")
                deviceHandler.setPlugState(0, "on")
        else:
            logging.info("Door is open")
            deviceHandler.setPlugState(0, "off")
        if value >= max:
            logging.info("High temperature detected")
            deviceHandler.setPlugState(0, "off")

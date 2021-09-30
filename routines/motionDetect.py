import sys
sys.path.append("..")
from config_data import deviceInfo
from utils import deviceHandler
import time
import logging

lastKitchen = deviceInfo.getPhilipsData("motion", 1, "last")
if (time.time() > lastKitchen + 60) and (deviceHandler.getLightState(1)):
    logging.info("No motion detected kitchen for 1 minute")
    deviceHandler.setLightState(1, "off")

lastHallway = deviceInfo.getPhilipsData("motion", 2, "last")
if (time.time() > lastHallway + 60) and (deviceHandler.getLightState(2)):
    logging.info("No motion detected hallway for 1 minute")
    deviceHandler.setLightState(2, "off")
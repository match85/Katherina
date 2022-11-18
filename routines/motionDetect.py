import sys
sys.path.append("..")
from utils import deviceHandler
from utils import statusHandler
import time
import logging

lastKitchen = statusHandler.getMotionLast(1)
if (time.time() > lastKitchen + 60) and (deviceHandler.getLightState(1)):
    logging.info("No motion detected kitchen for 1 minute")
    deviceHandler.setLightState(1, False)

lastHallway = statusHandler.getMotionLast(2)
if (time.time() > lastHallway + 60) and (deviceHandler.getLightState(2)):
    logging.info("No motion detected hallway for 1 minute")
    deviceHandler.setLightState(2, False)
    deviceHandler.turnOffWashTemp()

lastBath = statusHandler.getMotionLast(3)
if (time.time() > lastBath + 60) and (deviceHandler.getLightState(4)):
    logging.info("No motion detected bathroom for 1 minute")
    deviceHandler.setLightState(4, False)
#python3
import sys
sys.path.append("..")
from utils import statusHandler
from miio import ViomiVacuum
import time
import logging

vac = ViomiVacuum("192.168.1.185", "4c3852586a715070644c78664c426a6d")
cleaning = False
logging.info("Vacuum cleaning watching started")
while not cleaning:
    if not statusHandler.getPhoneState():
        logging.info("Starting vacuum cleaning")
        vac.start()
        cleaning = True
    else:
        logging.info("Vacuum cleaning: Phone detected, waiting for 30 minutes")
        time.sleep(1800)

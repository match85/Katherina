#python3
import sys
sys.path.append("..")
from utils import statusHandler
from miio import viomivacuum
import time

vac = viomivacuum.ViomiVacuum("192.168.1.185", "4c3852586a715070644c78664c426a6d")
cleaning = False

while not cleaning:
    if not statusHandler.getPhoneState():
        vac.start()
        cleaning = True
    else:
        time.sleep(1800)
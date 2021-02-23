import sys
sys.path.append("..")
from utils import deviceHandler
from prettyprinter import pprint

monitor = {
    "Plug 0 state": deviceHandler.getPlugState(0),
    "Plug 1 state": deviceHandler.getPlugState(1),
    "Light 1 state": deviceHandler.getLightState(1),
    "Light 2 state": deviceHandler.getLightState(2),
    "Light 3 state": deviceHandler.getLightState(3),
    "Light 4 state": deviceHandler.getLightState(4),
    "Current temperature": deviceHandler.getCurrentTemperature(1),
    "Min temperature": deviceHandler.getMinTemperature(1),
    "Max temperature": deviceHandler.getMaxTemperature(1),
    "Current humididy": deviceHandler.getCurrentHumidity(1),
    "Min humidity": deviceHandler.getMinHumidity(1),
    "Max humidity": deviceHandler.getMaxHumidity(1)
}

pprint(monitor)
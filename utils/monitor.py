import sys
sys.path.append("..")
from utils import deviceHandler

def getMonitor():
    monitor = {
        "Plug 0 state": deviceHandler.getPlugState(0),
        "Plug 1 state": deviceHandler.getPlugState(1),
        "Light 1 state": deviceHandler.getLightState(1),
        "Light 2 state": deviceHandler.getLightState(2),
        "Light 3 state": deviceHandler.getLightState(3),
        "Light 4 state": deviceHandler.getLightState(4),
        "Current temperature": deviceHandler.getCurrentTemperature(),
        "Min temperature": deviceHandler.getMinTemperature(),
        "Max temperature": deviceHandler.getMaxTemperature(),
        "Current humididy": deviceHandler.getCurrentHumidity(),
        "Min humidity": deviceHandler.getMinHumidity(),
        "Max humidity": deviceHandler.getMaxHumidity()
    }
    return monitor
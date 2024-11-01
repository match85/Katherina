import sys
sys.path.append("..")
from utils import deviceHandler
from utils import statusHandler

def getMonitor():
    monitor = {
        "Plug 0 state": deviceHandler.getPlugState(0),
        "Light 1 state": deviceHandler.getLightState(1),
        "Light 2 state": deviceHandler.getLightState(2),
        "Light 3 state": deviceHandler.getLightState(3),
        "Light 4 state": deviceHandler.getLightState(4),
        "Current temperature": statusHandler.getCurrentTemp(1),
        "Min temperature": deviceHandler.getMinTemperature(),
        "Max temperature": deviceHandler.getMaxTemperature(),
        "Current humididy": statusHandler.getCurrentHum(1),
        "Min humidity": deviceHandler.getMinHumidity(),
        "Max humidity": deviceHandler.getMaxHumidity()
    }
    return monitor
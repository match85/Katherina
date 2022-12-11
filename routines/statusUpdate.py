import sys

sys.path.append("..")
from utils import deviceHandler
from utils import statusHandler

statusHandler.setLightState(1, deviceHandler.getLightState(1))
statusHandler.setLightState(2, deviceHandler.getLightState(2))
statusHandler.setLightState(3, deviceHandler.getLightState(3))
statusHandler.setLightState(4, deviceHandler.getLightState(4))
statusHandler.setLightState(5, deviceHandler.getLightState(5))

statusHandler.setPlugState(0, deviceHandler.getPlugState(0))
statusHandler.setPlugState(1, deviceHandler.getPlugState(1))

statusHandler.writeOutStatus()
#python3
import sys
sys.path.append("..")

from config_data import deviceInfo
from utils import deviceHandler

"""
print(routineInfo.getRoutineData("temp", "min_temp"))
print(routineInfo.getRoutineData("comeHome", "enabled"))
print(routineInfo.getRoutineData("leftHome", "enabled"))
print(routineInfo.getRoutineData("dlinkMotion", "timeout"))

x = bool("true")
print(x)
"""
print(deviceHandler.getTabletUrl())
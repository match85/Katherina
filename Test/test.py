#python3
import sys
sys.path.append("..")
import socket
import time
from config_data import routineInfo
from utils import deviceHandler
from utils import databaseHandler

"""
print(routineInfo.getRoutineData("temp", "min_temp"))
print(routineInfo.getRoutineData("comeHome", "enabled"))
print(routineInfo.getRoutineData("leftHome", "enabled"))
print(routineInfo.getRoutineData("dlinkMotion", "timeout"))

x = bool("true")
print(x)
"""

routineInfo.setRoutineData("kitchenMotion", "minIlluminance", 2500)
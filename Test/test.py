#python3
import sys
sys.path.append("..")

from config_data import deviceInfo

"""
print(routineInfo.getRoutineData("temp", "min_temp"))
print(routineInfo.getRoutineData("comeHome", "enabled"))
print(routineInfo.getRoutineData("leftHome", "enabled"))
print(routineInfo.getRoutineData("dlinkMotion", "timeout"))

x = bool("true")
print(x)
"""
print(deviceInfo.getPhilipsData("hub", 1, "ip"))
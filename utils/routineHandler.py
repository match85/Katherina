#python3
from config_data import routineInfo

def isEnabled(routine):
    return routineInfo.getRoutineData(routine, "enabled")
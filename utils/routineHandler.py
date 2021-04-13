#python3
from config_data import routineInfo


def isEnabled(routine):
    if routineInfo.getRoutineData(routine, "enabled") == "True":
        return True
    else:
        return False
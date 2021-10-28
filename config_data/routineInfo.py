import json




def getRoutineData(routineName, item):
    with open("../config_data/routineConfig.json") as json_file:
        data = json.load(json_file)
    return data[routineName][item]


def setRoutineData(routine, item, value):
    with open("../config_data/routineConfig.json", "r+") as json_file:
        data = json.load(json_file)
        data[routine][item] = value
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()

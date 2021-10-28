import json

with open("../config_data/routineConfig.json") as json_file:
    data = json.load(json_file)

def getRoutineData(routineName, item):
    return data[routineName][item]

def setRoutineData(routine, item, value):
    data[routine][item] = value
    with open("../config_data/routineConfig.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
        json_file.truncate()



import json

with open("../config_data/routineConfig.json") as json_file:
    data = json.load(json_file)

def getRoutineData(routineName, item):
    return data[routineName][item]

"""
update = {
    "temp": {
        "enabled": "True"}
}

print(update)
"""


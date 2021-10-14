import sys

sys.path.append("..")
import json

with open("../config_data/status.json") as json_file:
    data = json.load(json_file)


def getMotionState(id):
    return data["motion"][str(id)]["state"]


def setMotionState(id, value):
    data["motion"][str(id)]["state"] = value
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)


def getMotionLast(id):
    return data["motion"][str(id)]["state"]


def setMotionLast(id, value):
    data["motion"][str(id)]["last"] = value
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)


def getLightState(id):
    return data["light"][str(id)]["state"]


def setLightState(id, value):
    data["light"][str(id)]["state"] = value
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)


def getPlugState(id):
    return data["plug"][str(id)]["state"]


def setPlugState(id, value):
    data["plug"][str(id)]["state"] = value
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)


def getCurrentTemp(id):
    return data["temp"][str(id)]["currentTemp"]


def setCurrentTemp(id, value):
    data["temp"][str(id)]["currentTemp"] = value
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)


def getCurrentHum(id):
    return data["temp"][str(id)]["currentHum"]


def setCurrentHum(id, value):
    data["temp"][str(id)]["currentHum"] = value
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)


def getDoorState(id):
    return data["door"][str(id)]["contact"]


def setDoorState(id, value):
    data["door"][str(id)]["contact"] = value
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)

import sys

sys.path.append("..")
import json

#with open("../config_data/status.json") as json_file:
#    data = json.load(json_file)


def getMotionState(id):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    return data["motion"][str(id)]["state"]


def setMotionState(id, value):
    with open("../config_data/status.json") as json_file:
        data = json.loads(json_file)
    data["motion"][str(id)]["state"] = value
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)


def getMotionLast(id):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    return data["motion"][str(id)]["last"]


def setMotionLast(id, value):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    data["motion"][str(id)]["last"] = value
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)


def getLightState(id):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    return data["light"][str(id)]["state"]


def setLightState(id, value):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    data["light"][str(id)]["state"] = value
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)


def getPlugState(id):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    return data["plug"][str(id)]["state"]


def setPlugState(id, value):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    data["plug"][str(id)]["state"] = value
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)


def getCurrentTemp(id):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    return data["temp"][str(id)]["currentTemp"]


def setCurrentTemp(id, value):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    data["temp"][str(id)]["currentTemp"] = value
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)


def getCurrentHum(id):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    return data["temp"][str(id)]["currentHum"]


def setCurrentHum(id, value):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    data["temp"][str(id)]["currentHum"] = value
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)


def getDoorState(id):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    return data["door"][str(id)]["contact"]


def setDoorState(id, value):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    data["door"][str(id)]["contact"] = value
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)

def setPhoneLast(last):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    data['phone']['last'] = last
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)

def getPhoneLast():
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    return data['phone']['last']

def setPhoneState(state):
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    data['phone']['state'] = state
    with open("../config_data/status.json", "w") as json_file:
        json.dump(data, json_file)

def getPhoneState():
    with open("../config_data/status.json") as json_file:
        data = json.load(json_file)
    return data['phone']['state']
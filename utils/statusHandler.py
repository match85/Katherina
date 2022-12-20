import sys

sys.path.append("..")
import json
import logging

#with open("../config_data/status.json") as json_file:
#    data = json.load(json_file)

if __name__ == "__main__":
    print("asdfd")

def getMotionState(id):
    with open("../config_data/status.json", "r") as json_file:
        data = json.load(json_file)
    return data["motion"][str(id)]["state"]


def setMotionState(id, value):
    with open("../config_data/status.json", "r+") as json_file:
        data = json.load(json_file)
        data["motion"][str(id)]["state"] = value
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()


def getMotionLast(id):
    with open("../config_data/status.json", "r") as json_file:
        data = json.load(json_file)
    return data["motion"][str(id)]["last"]


def setMotionLast(id, value):
    with open("../config_data/status.json", "r+") as json_file:
        data = json.load(json_file)
        data["motion"][str(id)]["last"] = value
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()


def getLightState(id):
    with open("../config_data/status.json", "r") as json_file:
        data = json.load(json_file)
    return data["light"][str(id)]["state"]


def setLightState(id, value):
    with open("../config_data/status.json", "r+") as json_file:
        data = json.load(json_file)
        data["light"][str(id)]["state"] = value
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()


def getPlugState(id):
    with open("../config_data/status.json", "r") as json_file:
        data = json.load(json_file)
    return data["plug"][str(id)]["state"]


def setPlugState(id, value):
    with open("../config_data/status.json", "r+") as json_file:
        data = json.load(json_file)
        data["plug"][str(id)]["state"] = value
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()


def getCurrentTemp(id):
    with open("../config_data/status.json", "r") as json_file:
        data = json.load(json_file)
    return data["temp"][str(id)]["currentTemp"]


def setCurrentTemp(id, value):
    with open("../config_data/status.json", "r+") as json_file:
        data = json.load(json_file)
        data["temp"][str(id)]["currentTemp"] = value
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()


def getCurrentHum(id):
    with open("../config_data/status.json", "r") as json_file:
        data = json.load(json_file)
    return data["temp"][str(id)]["currentHum"]


def setCurrentHum(id, value):
    with open("../config_data/status.json", "r+") as json_file:
        data = json.load(json_file)
        data["temp"][str(id)]["currentHum"] = value
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()


def getDoorState(id):
    with open("../config_data/status.json", "r") as json_file:
        data = json.load(json_file)
    return data["door"][str(id)]["contact"]


def setDoorState(id, value):
    with open("../config_data/status.json", "r+") as json_file:
        data = json.load(json_file)
        data["door"][str(id)]["contact"] = value
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()

def setPhoneLast(last):
    with open("../config_data/status.json", "r+") as json_file:
        data = json.load(json_file)
        data["phone"]["1"]["last"] = last
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()

def getPhoneLast():
    with open("../config_data/status.json", "r") as json_file:
        data = json.load(json_file)
    return data["phone"]["1"]["last"]

def setPhoneState(state):
    with open("../config_data/status.json", "r+") as json_file:
        data = json.load(json_file)
        data["phone"]["1"]["state"] = state
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()

def getPhoneState():
    with open("../config_data/status.json", "r") as json_file:
        data = json.load(json_file)
    return data["phone"]["1"]["state"]
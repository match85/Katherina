import json
import importlib

with open("../config_data/deviceConfig.json") as json_file:
    data = json.load(json_file)

def getFlaskIp():
    return data["flask"]["ip"]

def getFlaskPort():
    return data["flask"]["port"]

def getRpiIp():
    return data["raspberry"]["ip"]

def getDynamoUrl():
    return data["dynamo"]["url"]

def getPhoneIp():
    return data["phone"]["ip"]

def getTabletIp():
    return data["tablet"]["ip"]

def getTabletPort():
    return data["tablet"]["port"]

def getPhilipsData(type, id, item):
    return data["philips"][type][str(id)][item]

def getDlinkData(type, id, item):
    return data["dlink"][type][str(id)][item]

def setPhilipsData(type, id, item, value):
    data["philips"][type][str(id)][item] = value
    with open("../config_data/deviceConfig.json", "w") as json_file:
        json.dump(data, json_file)
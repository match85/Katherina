import json

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

def getPhilipsData(type, id, item):
    return data["philips"][type][id][item]

def getDlinkData(type, id, item):
    return data["dlink"][type][str(id)][item]
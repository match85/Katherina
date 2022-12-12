import sys

sys.path.append("..")
import json
import logging
from datetime import date
today = date.today()
logging.basicConfig(filename='../logs/' + str(today) + '.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.INFO)


with open("../config_data/status.json", "r+") as json_file:
    data = json.load(json_file)
    logging.info("Status.json loaded")

    def writeOutStatus():
        with open("../config_data/status.json", "r+") as json_file2:
            json_file2.seek(0)
            json.dump(data, json_file2, indent=4)
            json_file2.truncate()


    def getMotionState(id):
        return data["motion"][str(id)]["state"]


    def setMotionState(id, value):
        data["motion"][str(id)]["state"] = value


    def getMotionLast(id):
        return data["motion"][str(id)]["last"]


    def setMotionLast(id, value):
        data["motion"][str(id)]["last"] = value


    def getLightState(id):
        return data["light"][str(id)]["state"]


    def setLightState(id, value):
        data["light"][str(id)]["state"] = value


    def getPlugState(id):
        return data["plug"][str(id)]["state"]


    def setPlugState(id, value):
        data["plug"][str(id)]["state"] = value


    def getCurrentTemp(id):
        with open("../config_data/status.json", "r") as json_file:
            data = json.load(json_file)
        return data["temp"][str(id)]["currentTemp"]


    def setCurrentTemp(id, value):
        data["temp"][str(id)]["currentTemp"] = value


    def getCurrentHum(id):
        return data["temp"][str(id)]["currentHum"]


    def setCurrentHum(id, value):
        data["temp"][str(id)]["currentHum"] = value


    def getDoorState(id):
        return data["door"][str(id)]["contact"]


    def setDoorState(id, value):
        data["door"][str(id)]["contact"] = value


    def setPhoneLast(last):
        data["phone"]["1"]["last"] = last


    def getPhoneLast():
        return data["phone"]["1"]["last"]


    def setPhoneState(state):
        data["phone"]["1"]["state"] = state


    def getPhoneState():
        return data["phone"]["1"]["state"]

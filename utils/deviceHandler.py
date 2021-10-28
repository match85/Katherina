# python3
import json
import platform
import subprocess
import time

from config_data import deviceInfo
from config_data import routineInfo
from utils import deviceHandler
import requests
from datetime import date
from utils import statusHandler

today = date.today()
import logging

logging.basicConfig(filename='../logs/' + str(today) + '.log', format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S', level=logging.INFO)

from utils.pyS150 import MotionSensor
from utils.pyW215 import SmartPlug, ON, OFF

# from utils import databaseHandler

hubUrl = "http://" + deviceInfo.getPhilipsData("hub", "1", "ip") + "/api/" + deviceInfo.getPhilipsData("hub", "1",
                                                                                                       "auth")


# Phone check
def getPhoneState(timeout):
    return True

    '''
    logging.info("Checking phone state with timeout " + str(timeout) + " minutes")
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    param2 = '-w' if platform.system().lower() == 'windows' else '-W'
    command = ['ping', param, '1', param2, '1', deviceInfo.getPhoneIp()]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    response = str(out).lower().find("ttl")
    if response == -1:
        presence = False
        statusHandler.setPhoneState(False)
    else:
        presence = True
        statusHandler.setPhoneLast(time.time())
        statusHandler.setPhoneState(True)

    if response == -1 and timeout > 0:
        i = 0

        while (presence != True) and (i < timeout):
            time.sleep(60)
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()
            response = str(out).lower().find("ttl")
            if response == -1:
                i += 1
            else:
                presence = True
    if presence:
        statusHandler.setPhoneLast(time.time())
        statusHandler.setPhoneState(True)
        logging.info("Phone detected in " + str(timeout) + " minutes")
    else:
        statusHandler.setPhoneState(False)
        logging.info("No phone detected in " + str(timeout) + " minutes")

    return presence
    '''

# DLink
##Motion

def getMotionState():
    x = MotionSensor(deviceInfo.getDlinkData("motion", "1", "ip"), deviceInfo.getDlinkData("motion", "1", "auth"))
    return int(x.state)


# Philips
##Lights

def setLightState(id, state):
    url = hubUrl + "/lights/" + str(id) + "/state"
    if state == 'on':
        data = {"on": True}
    else:
        data = {"on": False}
    logging.info("Switching " + state + " " + getLightName(id) + "(" + str(id) + ") light")
    r = requests.put(url, json.dumps(data), timeout=5)
    try:
        requests.get(deviceHandler.getTabletUrl() + "light" + str(id) + "=" + str(state))
    except:
        pass
    return 'OK'


def getLightState(id):
    url = hubUrl + "/lights/" + str(id)
    r = requests.get(url)
    data = r.json()
    return data['state']['on']


def setLightBrightness(id, level):
    url = hubUrl + "/lights/" + str(id) + "/state"

    data = {"bri": int(level)}
    logging.info("Set " + getLightName(id) + "(" + str(id) + ") brightness to " + str(level))
    r = requests.put(url, json.dumps(data), timeout=5)
    return 'OK'


def getLightName(id):
    return deviceInfo.getPhilipsData("light", str(id), "name")


##MotionSensors

def getSensorPresence(id):
    url = hubUrl + "/sensors/" + str(id)
    r = requests.get(url)
    data = r.json()
    return str(data["state"]["presence"])


def getSensorLightlevel(id):
    url = hubUrl + "/sensors/" + str(id)
    r = requests.get(url)
    data = r.json()
    return str(data["state"]["lightlevel"])


# DLink
##Plugs

def setPlugState(id, state):
    sp = SmartPlug(deviceInfo.getDlinkData("plug", id, "ip"), deviceInfo.getDlinkData("plug", id, "auth"))
    logging.info("Turning " + state + " " + getPlugName(id) + "(" + str(id) + ")")
    if state == 'on':
        sp.state = ON
    else:
        sp.state = OFF
    try:
        requests.get(deviceHandler.getTabletUrl() + "plug" + str(id) + "=" + str(state))
    except:
        pass
    return 'OK'


def getPlugState(id):
    sp = SmartPlug(deviceInfo.getDlinkData("plug", id, "ip"), deviceInfo.getDlinkData("plug", id, "auth"))
    return str(sp.state)


def getPlugName(id):
    return deviceInfo.getDlinkData("plug", id, "name")


# Shelly
##H&T Sensor

def getCurrentTemperature():
    return routineInfo.getRoutineData("temp", "current_temp")


def getMinTemperature():
    return routineInfo.getRoutineData("temp", "min_temp")


def getMaxTemperature():
    return routineInfo.getRoutineData("temp", "max_temp")


def setMinTemperature(value):
    return routineInfo.setRoutineData("temp", "min_temp", str(value))


def setMaxTemperature(value):
    return routineInfo.setRoutineData("temp", "max_temp", str(value))


def getCurrentHumidity():
    return routineInfo.getRoutineData("temp", "current_hum")


def getMinHumidity():
    return routineInfo.getRoutineData("temp", "min_hum")


def getMaxHumidity():
    return routineInfo.getRoutineData("temp", "max_hum")


def setMinHumidity(value):
    return routineInfo.setRoutineData("temp", "min_hum", str(value))


def setMaxHumidity(value):
    return routineInfo.setRoutineData("temp", "max_hum", str(value))


def getTabletUrl():
    return "http://" + deviceInfo.getTabletIp() + ":" + deviceInfo.getTabletPort() + "/?"

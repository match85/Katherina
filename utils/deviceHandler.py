# python3
import json
import time

import yeelight

from config_data import deviceInfo
from config_data import routineInfo
from utils import deviceHandler
import requests
from datetime import date, datetime
from utils import statusHandler
import os
from yeelight import Bulb
import paho.mqtt.client as mqtt

today = date.today()
import logging

logging.basicConfig(filename='../logs/' + str(today) + '.log', format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S', level=logging.INFO)

from utils.pyS150 import MotionSensor
from utils.pyW215 import SmartPlug, ON, OFF

hubUrl = "http://" + deviceInfo.getPhilipsData("hub", "1", "ip") + "/api/" + deviceInfo.getPhilipsData("hub", "1",
                                                                                                       "auth")

def goneHome():
    if ((datetime.now().hour >= 17) or (datetime.now().hour <= 5)) and ((statusHandler.getPhoneLast() + 1800) < time.time()):
        return True
    else:
        return False


# DLink
##Motion

def getMotionState():
    x = MotionSensor(deviceInfo.getDlinkData("motion", "1", "ip"), deviceInfo.getDlinkData("motion", "1", "auth"))
    return int(x.state)


# Yeelight
##Lights


def setLightState(id, state):
    bulb_room = yeelight.Bulb("192.168.1.160")
    bulb_bath = yeelight.Bulb("192.168.1.161")
    bulb_hallway = yeelight.Bulb("192.168.1.162")
    bulb_kitchen = yeelight.Bulb("192.168.1.163")
    if id == 3:
        if getLightState(id) != state:
            if state:
                try:
                    logging.info("Setting light " + getLightName(id) + "(" + str(id) + ") to " + str(state))
                    bulb_room.turn_on()
                except yeelight.BulbException:
                    pass
            if not state:
                try:
                    logging.info("Setting light " + getLightName(id) + "(" + str(id) + ") to " + str(state))
                    bulb_room.turn_off()
                except yeelight.BulbException:
                    pass
        statusHandler.setLightState(id, state)
    if id == 4:
        if getLightState(id) != state:
            if state:
                logging.info("Setting light " + getLightName(id) + "(" + str(id) + ") to " + str(state))
                bulb_bath.turn_on()
            if not state:
                try:
                    logging.info("Setting light " + getLightName(id) + "(" + str(id) + ") to " + str(state))
                    bulb_bath.turn_off()
                except yeelight.BulbException:
                    pass
        statusHandler.setLightState(id, state)
    if id == 2:
        if getLightState(id) != state:
            if state:
                try:
                    logging.info("Setting light " + getLightName(id) + "(" + str(id) + ") to " + str(state))
                    bulb_hallway.turn_on()
                except yeelight.BulbException as err:
                    print(err)
                    pass
            if not state:
                try:
                    logging.info("Setting light " + getLightName(id) + "(" + str(id) + ") to " + str(state))
                    bulb_hallway.turn_off()
                except yeelight.BulbException as err:
                    print(err)
                    pass
        statusHandler.setLightState(id, state)
    if id == 1:
        if getLightState(id) != state:
            if state:
                try:
                    logging.info("Setting light " + getLightName(id) + "(" + str(id) + ") to " + str(state))
                    bulb_kitchen.turn_on()
                except yeelight.BulbException:
                    pass
            if not state:
                try:
                    logging.info("Setting light " + getLightName(id) + "(" + str(id) + ") to " + str(state))
                    bulb_kitchen.turn_off()
                except yeelight.BulbException:
                    pass
        statusHandler.setLightState(id, state)
    try:
        requests.get(deviceHandler.getTabletUrl() + "light" + str(id) + "=" + str(state), timeout=1)
    except:
        pass
        return 'OK'


def getLightState(id):
    bulb_room = yeelight.Bulb("192.168.1.160")
    bulb_bath = yeelight.Bulb("192.168.1.161")
    bulb_hallway = yeelight.Bulb("192.168.1.162")
    bulb_kitchen = yeelight.Bulb("192.168.1.163")
    if id == 3:
        try:
            data = bulb_room.get_properties()["power"]
        except yeelight.BulbException:
            return False
        if data == "on":
            return True
        if data == "off":
            return False
    if id == 4:
        try:
            data = bulb_bath.get_properties()["power"]
        except yeelight.BulbException:
            return False
        if data == "on":
            return True
        if data == "off":
            return False
    if id == 2:
        try:
            data = bulb_hallway.get_properties()["power"]
        except yeelight.BulbException:
            return False
        if data == "on":
            return True
        if data == "off":
            return False
    if id == 1:
        try:
            data = bulb_kitchen.get_properties()["power"]
        except yeelight.BulbException:
            return False
        if data == "on":
            return True
        if data == "off":
            return False


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
        requests.get(deviceHandler.getTabletUrl() + "plug" + str(id) + "=" + str(state), timeout=1)
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

def alexaSay(text):
    logging.info(os.system(r'/home/pi/alexa-remote-control-master/alexa_remote_control.sh -d ALL -e speak:\"' + text + '\"'))


def turnOffWashTemp():
    client = mqtt.Client(deviceInfo.getRpiIp())
    client.connect(deviceInfo.getRpiIp())
    client.publish("zigbee2mqtt/washroom_light/set", "{\"state\": \"OFF\"}")
    client.disconnect()
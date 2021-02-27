#python3
import json
import platform
import subprocess
import time

from config_data import init_config
import requests
from datetime import date
today = date.today()
import logging
logging.basicConfig(filename='../logs/' + str(today) + '.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.INFO)

from utils.pyS150 import MotionSensor
from utils.pyW215 import SmartPlug, ON, OFF
from utils import databaseHandler

hubUrl = "http://" + init_config.getPhilipsIp() + "/api/" + init_config.getPhilipsAuth()

#Phone check
def getPhoneState(timeout):
	param = '-n' if platform.system().lower() == 'windows' else '-c'
	param2 = '-w' if platform.system().lower() == 'windows' else '-W'
	command = ['ping', param, '1', param2, '1', init_config.getPhoneIp()]
	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = process.communicate()
	response = str(out).lower().find("ttl")
	if response == -1:
		presence = False
	else:
		presence = True

	if timeout == 0:
		return presence

	if response == -1:
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
	return presence

#DLink
##Motion

def getMotionState():
    x = MotionSensor(init_config.getDlinkMotionIp(), init_config.getDlinkMotionAuth())
    return int(x.state)


#Philips
##Lights

def setLightState(id, state):
	url = hubUrl + "/lights/" + str(id) + "/state"
	if state == 'on':
		data = {"on":True}
	else:
		data = {"on":False}
	r = requests.put(url, json.dumps(data), timeout=5)
	return 'OK'

def getLightState(id):
	url = hubUrl + "/lights/" + str(id)
	r = requests.get(url)
	data = r.json()
	return data['state']['on']

def setLightBrightness(id, level):
	url = hubUrl + "/lights/" + str(id) + "/state"

	data = {"bri":level}
	r = requests.put(url, json.dumps(data), timeout=5)
	return 'OK'

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



#DLink
##Plugs

def setPlugState(id, state):
	sp = SmartPlug(init_config.getDlinkPlugIp(id), init_config.getDlinkPlugAuth(id))
	if state == 'on':
		sp.state = ON
	else:
		sp.state = OFF
	return 'OK'

def getPlugState(id):
	sp = SmartPlug(init_config.getDlinkPlugIp(id), init_config.getDlinkPlugAuth(id))
	return str(sp.state)


#Shelly
##H&T Sensor

def getCurrentTemperature(id):
	return databaseHandler.getCurrentTemperature(id)

def getMinTemperature(id):
	return databaseHandler.getMinTemperature(id)

def getMaxTemperature(id):
	return databaseHandler.getMaxTemperature(id)

def setCurrentTemperature(id, value):
	return databaseHandler.setCurrentTemperature(id, value)

def setMinTemperature(id, value):
	return databaseHandler.setMinTemperature(id, value)

def setMaxTemperature(id, value):
	return databaseHandler.getMaxTemperature(id, value)

def setCurrentHumidity(id, value):
	return databaseHandler.setCurrentHumidity(id, value)

def getCurrentHumidity(id):
	return databaseHandler.getCurrentHumidity(id)

def getMinHumidity(id):
	return databaseHandler.getMinHumidity(id)

def getMaxHumidity(id):
	return databaseHandler.getMaxHumidity(id)

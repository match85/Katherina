#python3
import json

from config_data import init_config
import requests

from utils.pyS150 import MotionSensor
from utils.pyW215 import SmartPlug, ON, OFF

hubUrl = "http://" + init_config.getPhilipsIp() + "/api/" + init_config.getPhilipsAuth()

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
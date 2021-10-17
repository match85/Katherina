import paho.mqtt.client as mqtt
import sys
sys.path.append("..")
import time
import json
import socket
import requests
from utils import deviceHandler
from utils import statusHandler
from config_data import routineInfo
from config_data import deviceInfo
import importlib

from datetime import date
today = date.today()
import logging
logging.basicConfig(filename='../logs/' + str(today) + '.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.INFO)

kitchenMotion = deviceInfo.getPhilipsData('motion', 1, 'zigbeeName')
hallwayMotion = deviceInfo.getPhilipsData('motion', 2, 'zigbeeName')
doorSensor = deviceInfo.getXiaomiData('door', 1, 'zigbeeName')

def on_message(client, userdata, message):
    #print("received message: " ,str(message.payload.decode("utf-8")))
    importlib.reload(routineInfo)
    #print(message.topic)
    if message.topic == kitchenMotion:
        response = json.loads(message.payload.decode("utf8"))
        #deviceInfo.setPhilipsData("motion", 1, "state", response['occupancy'])
        statusHandler.setMotionState(1, response['occupancy'])
        now = time.localtime()
        print("Kitchen: " + time.strftime("%H:%M:%S", now), "Presence: " + str(response['occupancy']) + " Illuminance: " + str(response['illuminance']) + " Lux: " + str(response['illuminance_lux']))
        if bool(response['occupancy']):
            #logging.info("Motion detected in kitchen")
            #deviceInfo.setPhilipsData("motion", 1, "last", time.time())
            statusHandler.setMotionLast(1, time.time())
            if not deviceHandler.getLightState(2):
                if int(response['illuminance']) < routineInfo.getRoutineData("kitchenMotion", "minIlluminance"):
                    deviceHandler.setLightState(1, "on")
            else:
                deviceHandler.setLightState(1, "on")
            #time.sleep(60)
        '''
        else:
            #logging.info("No motion detected in kitchen")
            if deviceHandler.getLightState(1) and not bool(response['occupancy']):
                deviceHandler.setLightState(1, "off")
        '''
    if message.topic == hallwayMotion:
        response = json.loads(message.payload.decode("utf8"))
        #deviceInfo.setPhilipsData("motion", 2, "state", response['occupancy'])
        statusHandler.setMotionState(2, response['occupancy'])
        now = time.localtime()
        print("Hallway: " + time.strftime("%H:%M:%S", now), "Presence: " + str(response['occupancy']) + " Illuminance: " + str(response['illuminance']) + " Lux: " + str(response['illuminance_lux']))
        print(routineInfo.getRoutineData("kitchenMotion", "minIlluminance"))
        if bool(response['occupancy']):
            #logging.info("Motion detected in hallway")
            #deviceInfo.setPhilipsData("motion", 2, "last", time.time())
            statusHandler.setMotionLast(2, time.time())
            if not deviceHandler.getLightState(1):
                if int(response['illuminance']) < routineInfo.getRoutineData("kitchenMotion", "minIlluminance"):
                    deviceHandler.setLightState(2, "on")
            else:
                deviceHandler.setLightState(2, "on")
            try:
                requests.get(deviceHandler.getTabletUrl() + "motion=true")
            except:
                pass
        # time.sleep(60)
        else:
            #logging.info("No motion detected in hallway")
            if deviceHandler.getLightState(2) and not bool(response['occupancy']):
                deviceHandler.setLightState(2, "off")

    if message.topic == doorSensor:
        response = json.loads(message.payload.decode("utf8"))
        statusHandler.setDoorState(1, response['contact'])
        logging.info("Door sensor " + str(response['contact']))

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True #set flag
        #print("connected OK")
        client.subscribe(kitchenMotion)
        client.subscribe(hallwayMotion)
        client.subscribe(doorSensor)
    else:
        print("Bad connection Returned code=", rc)
        client.bad_connection_flag = True

#time.sleep(60)
mqttBroker ="192.168.1.100"
mqtt.Client.connected_flag=False
client = mqtt.Client(socket.gethostname())
client.on_connect = on_connect
client.loop_start()
print("Connecting to broker ", mqttBroker)
client.connect(mqttBroker)
while not client.connected_flag:
    print("In wait loop")
    time.sleep(1)
print("in Main Loop")
while True:
    client.on_message = on_message


#time.sleep(30)
client.loop_stop()
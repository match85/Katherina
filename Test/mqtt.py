from datetime import date

import paho.mqtt.client as mqtt
import sys
sys.path.append("..")
import os
import time
import json
import socket
import requests
from utils import deviceHandler
from utils import statusHandler
from config_data import routineInfo
from config_data import deviceInfo
import importlib


today = date.today()
import logging
logging.basicConfig(filename='../logs/' + str(today) + '.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.INFO)

kitchenMotion = deviceInfo.getPhilipsData('motion', 1, 'zigbeeName')
hallwayMotion = deviceInfo.getPhilipsData('motion', 2, 'zigbeeName')
doorSensor = deviceInfo.getXiaomiData('door', 1, 'zigbeeName')
switch = deviceInfo.getPhilipsData('switch', 1, 'zigbeeName')

def on_message(client, userdata, message):
    #print("received message: " ,str(message.payload.decode("utf-8")))
    importlib.reload(routineInfo)
    #print(message.topic)
    if message.topic == kitchenMotion:
        response = json.loads(message.payload.decode("utf8"))
        print(response)
        #deviceInfo.setPhilipsData("motion", 1, "state", response['occupancy'])
        statusHandler.setMotionState(1, response['occupancy'])
        now = time.localtime()
        print("Kitchen: " + time.strftime("%H:%M:%S", now), "Presence: " + str(response['occupancy']) + " Illuminance: " + str(response['illuminance']) + " Lux: " + str(response['illuminance_lux']))
        if response['occupancy']:
            #logging.info("Motion detected in kitchen")
            #deviceInfo.setPhilipsData("motion", 1, "last", time.time())
            statusHandler.setMotionLast(1, time.time())
            if not statusHandler.getLightState(2):
                if int(response['illuminance']) < routineInfo.getRoutineData("kitchenMotion", "minIlluminance"):
                    deviceHandler.setLightState(1, True)
            else:
                deviceHandler.setLightState(1, True)

    if message.topic == hallwayMotion:
        response = json.loads(message.payload.decode("utf8"))
        print(response)
        #deviceInfo.setPhilipsData("motion", 2, "state", response['occupancy'])
        statusHandler.setMotionState(2, response['occupancy'])
        now = time.localtime()
        print("Hallway: " + time.strftime("%H:%M:%S", now), "Presence: " + str(response['occupancy']) + " Illuminance: " + str(response['illuminance']) + " Lux: " + str(response['illuminance_lux']))
        print(routineInfo.getRoutineData("kitchenMotion", "minIlluminance"))
        if response['occupancy']:
            #logging.info("Motion detected in hallway")
            #deviceInfo.setPhilipsData("motion", 2, "last", time.time())
            statusHandler.setMotionLast(2, time.time())
            if not statusHandler.getLightState(1):
                if int(response['illuminance']) < routineInfo.getRoutineData("kitchenMotion", "minIlluminance"):
                    deviceHandler.setLightState(2, True)
            else:
                deviceHandler.setLightState(2, True)

            if deviceHandler.goneHome():
                deviceHandler.setLightState(3, True)
            try:
                requests.get(deviceHandler.getTabletUrl() + "motion=true")
            except:
                pass
        #else:
            #logging.info("No motion detected in hallway")
        #    if statusHandler.getLightState(2) and not response['occupancy']:
        #        deviceHandler.setLightState(2, False)

    if message.topic == doorSensor:
        response = json.loads(message.payload.decode("utf8"))
        print(response)
        statusHandler.setDoorState(1, response['contact'])
        logging.info("Door sensor " + str(response['contact']))

    if message.topic == switch:
        response = json.loads(message.payload.decode("utf8"))
        try:
            if response['action'] == 'on-press':
                if not statusHandler.getLightState(3):
                    deviceHandler.setLightState(3, True)
                else:
                    deviceHandler.setLightState(3, False)

            if response['action'] == 'off-press':
                print('off button')

            if response['action'] == 'up-press':
                min_temp = float(routineInfo.getRoutineData("temp", "min_temp"))
                max_temp = float(routineInfo.getRoutineData("temp", "max_temp"))
                routineInfo.setRoutineData("temp", "min_temp", str(min_temp + 1))
                routineInfo.setRoutineData("temp", "max_temp", str(max_temp + 1))
                text = "Temperature increased to " + routineInfo.getRoutineData("temp", "min_temp") + "-" + routineInfo.getRoutineData("temp", "max_temp")
                logging.info("Temperature increased to " + routineInfo.getRoutineData("temp", "min_temp") + "-" + routineInfo.getRoutineData("temp", "max_temp"))
                os.system('/home/pi/alexa-remote-control-master/alexa_remote_control.sh -d ALL -e speak:\"' + text + '\"')

            if response['action'] == 'down-press':
                min_temp = float(routineInfo.getRoutineData("temp", "min_temp"))
                max_temp = float(routineInfo.getRoutineData("temp", "max_temp"))
                routineInfo.setRoutineData("temp", "min_temp", str(min_temp - 1))
                routineInfo.setRoutineData("temp", "max_temp", str(max_temp - 1))
                text = "Temperature decreased to " + routineInfo.getRoutineData("temp", "min_temp") + "-" + routineInfo.getRoutineData("temp", "max_temp")
                logging.info("Temperature decreased to " + routineInfo.getRoutineData("temp", "min_temp") + "-" + routineInfo.getRoutineData("temp", "max_temp"))
                os.system('/home/pi/alexa-remote-control-master/alexa_remote_control.sh -d ALL -e speak:\"' + text + '\"')

        except:
            pass


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        #print("connected OK")
        client.subscribe(kitchenMotion)
        client.subscribe(hallwayMotion)
        client.subscribe(doorSensor)
        client.subscribe(switch)
    else:
        print("Bad connection Returned code=", rc)
        client.bad_connection_flag = True


mqttBroker = deviceInfo.getRpiIp()
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
from datetime import date

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
import logging

today = date.today()
logging.basicConfig(filename='../logs/' + str(today) + '.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)

kitchenMotion = deviceInfo.getPhilipsData('motion', 1, 'zigbeeName')
hallwayMotion = deviceInfo.getPhilipsData('motion', 2, 'zigbeeName')
doorSensor = deviceInfo.getXiaomiData('door', 1, 'zigbeeName')
switch = deviceInfo.getPhilipsData('switch', 1, 'zigbeeName')

def on_message(client, userdata, message):
    try:
        importlib.reload(routineInfo)
        response = json.loads(message.payload.decode("utf8"))
        logging.info("Message received: " + str(message.topic))
        if message.topic == kitchenMotion:
            statusHandler.setMotionState(1, response['occupancy'])
            if response['occupancy']:
                logging.info("Motion detected in kitchen")
                statusHandler.setMotionLast(1, time.time())
                if not statusHandler.getLightState(2):
                    if int(response['illuminance']) < routineInfo.getRoutineData("kitchenMotion", "minIlluminance"):
                        deviceHandler.setLightState(1, True)
                else:
                    deviceHandler.setLightState(1, True)

        if message.topic == hallwayMotion:
            statusHandler.setMotionState(2, response['occupancy'])
            if response['occupancy']:
                logging.info("Motion detected in hallway")
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

        if message.topic == 'zigbee2mqtt/bath_motion':
            statusHandler.setMotionState(3, response['occupancy'])
            if response['occupancy']:
                logging.info("Motion detected in bathroom")
                statusHandler.setMotionLast(3, time.time())
                deviceHandler.setLightState(4, True)

        if message.topic == doorSensor:
            statusHandler.setDoorState(1, response['contact'])
            logging.info("Door sensor " + str(response['contact']))

        if message.topic == switch:
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
                    routineInfo.setRoutineData("temp", "min_temp", str(min_temp + 0.5))
                    routineInfo.setRoutineData("temp", "max_temp", str(max_temp + 0.5))
                    #text = "Temperature increased to " + routineInfo.getRoutineData("temp", "min_temp") + "-" + routineInfo.getRoutineData("temp", "max_temp")
                    logging.info("Temperature increased to " + routineInfo.getRoutineData("temp", "min_temp") + "-" + routineInfo.getRoutineData("temp", "max_temp"))
                    #deviceHandler.alexaSay(text)

                if response['action'] == 'down-press':
                    min_temp = float(routineInfo.getRoutineData("temp", "min_temp"))
                    max_temp = float(routineInfo.getRoutineData("temp", "max_temp"))
                    routineInfo.setRoutineData("temp", "min_temp", str(min_temp - 0.5))
                    routineInfo.setRoutineData("temp", "max_temp", str(max_temp - 0.5))
                    #text = "Temperature decreased to " + routineInfo.getRoutineData("temp", "min_temp") + "-" + routineInfo.getRoutineData("temp", "max_temp")
                    logging.info("Temperature decreased to " + routineInfo.getRoutineData("temp", "min_temp") + "-" + routineInfo.getRoutineData("temp", "max_temp"))
                    #deviceHandler.alexaSay(text)

            except:
                pass
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
        client.subscribe('zigbee2mqtt/bath_motion')
    else:
        print("Bad connection Returned code=", rc)
        client.bad_connection_flag = True


mqttBroker = deviceInfo.getRpiIp()
mqtt.Client.connected_flag=False
client = mqtt.Client(socket.gethostname())
client.enable_logger()
client.on_connect = on_connect
client.on_message = on_message
print("Connecting to broker ", mqttBroker)
client.connect(mqttBroker)
client.loop_forever()
client.loop_stop()
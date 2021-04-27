import paho.mqtt.client as mqtt
import sys
sys.path.append("..")
import time
import json
import socket
import requests
from utils import deviceHandler
from config_data import routineInfo
from config_data import deviceInfo
import importlib

def on_message(client, userdata, message):
    #print("received message: " ,str(message.payload.decode("utf-8")))
    #print(message.topic)
    importlib.reload(routineInfo)
    if message.topic == "zigbee2mqtt/0x001788010202e78e":
        response = json.loads(message.payload.decode("utf8"))
        deviceInfo.setPhilipsData("motion", 1, "state", response['occupancy'])
        now = time.localtime()
        print("Kitchen: " + time.strftime("%H:%M:%S", now), "Presence: " + str(response['occupancy']) + " Illuminance: " + str(response['illuminance']) + " Lux: " + str(response['illuminance_lux']))
        if bool(response['occupancy']):
            if not deviceHandler.getLightState(2):
                if int(response['illuminance']) < routineInfo.getRoutineData("kitchenMotion", "minIlluminance"):
                    deviceHandler.setLightState(1, "on")
            else:
                deviceHandler.setLightState(1, "on")
            #time.sleep(60)
        else:
            if deviceHandler.getLightState(1) and not bool(response['occupancy']):
                deviceHandler.setLightState(1, "off")
    if message.topic == "zigbee2mqtt/0x0017880102109f7e":
        response = json.loads(message.payload.decode("utf8"))
        deviceInfo.setPhilipsData("motion", 2, "state", response['occupancy'])
        now = time.localtime()
        print("Hallway: " + time.strftime("%H:%M:%S", now), "Presence: " + str(response['occupancy']) + " Illuminance: " + str(response['illuminance']) + " Lux: " + str(response['illuminance_lux']))
        print(routineInfo.getRoutineData("kitchenMotion", "minIlluminance"))
        if bool(response['occupancy']):
            requests.get(deviceHandler.getTabletUrl() + "motion=true")
            if not deviceHandler.getLightState(1):
                if int(response['illuminance']) < routineInfo.getRoutineData("kitchenMotion", "minIlluminance"):
                    deviceHandler.setLightState(2, "on")
            else:
                deviceHandler.setLightState(2, "on")
        # time.sleep(60)
        else:
            if deviceHandler.getLightState(2) and not bool(response['occupancy']):
                deviceHandler.setLightState(2, "off")


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True #set flag
        #print("connected OK")
        client.subscribe("zigbee2mqtt/0x001788010202e78e")
        client.subscribe("zigbee2mqtt/0x0017880102109f7e")
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
import paho.mqtt.client as mqtt
import sys
sys.path.append("..")
import time
import json
import socket
from utils import deviceHandler

def on_message(client, userdata, message):
    #print("received message: " ,str(message.payload.decode("utf-8")))
    response = json.loads(message.payload.decode("utf8"))
    print("Presence: " + str(response['occupancy']) + " Illuminance: " + str(response['illuminance']) + " Lux: " + str(response['illuminance_lux']))
    if bool(response['occupancy']) and (int(response['illuminance']) < 3000):
        deviceHandler.setLightState(1, "on")
        #time.sleep(60)
    else:
        if deviceHandler.getLightState(1) and not bool(response['occupancy']):
            deviceHandler.setLightState(1, "off")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True #set flag
        #print("connected OK")
        client.subscribe("zigbee2mqtt/0x001788010202e78e")
    else:
        print("Bad connection Returned code=", rc)
        client.bad_connection_flag = True

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
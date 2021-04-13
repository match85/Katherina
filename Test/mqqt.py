import paho.mqtt.client as mqtt
import time
import json
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

mqttBroker ="192.168.1.100"

client = mqtt.Client("Smartphone")
client.connect(mqttBroker)

client.loop_start()

client.subscribe("zigbee2mqtt/0x001788010202e78e")
print(client.is_connected())
while True:
    client.on_message=on_message


#time.sleep(30)
client.loop_stop()
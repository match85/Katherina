#python3

import time
import os
import requests
import databaseHandler

min = databaseHandler.getMinTemperature(1)
max = databaseHandler.getMaxTemperature(1)
r = os.system("ping -c 1 -W 1 192.168.1.101")
print(r)
if r != 0:
	requests.get("http://192.168.1.100:6969/plugs/0/off")
else:
	#file = open("/tmp/tempRep.txt", "r")
	#value = float(file.read())
	value = databaseHandler.getCurrentTemperature(1)
	#print(value)
	if value <= min:
		requests.get("http://192.168.1.100:6969/plugs/0/on")
	if value >= max:
		requests.get("http://192.168.1.100:6969/plugs/0/off")
#time.sleep(60)
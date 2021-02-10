#python3

import os
import requests
from utils import databaseHandler

min = databaseHandler.getMinTemperature(1)
max = databaseHandler.getMaxTemperature(1)
r = os.system("ping -c 1 192.168.1.101")
print(r)
if r != 0:
	requests.get("http://192.168.1.100:6969/plugs/0/off")
else:
	value = databaseHandler.getCurrentTemperature(1)
	if value <= min:
		requests.get("http://192.168.1.100:6969/plugs/0/on")
	if value >= max:
		requests.get("http://192.168.1.100:6969/plugs/0/off")
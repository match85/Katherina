import requests
import json
import os
import time
from utils import deviceHandler

url5 = "http://192.168.1.100:6969/plugs/0/off"


r = os.system("ping -c 1 -w 1 192.168.1.101")

if r != 0:
	i = 0
	left = True
	while left and (i < 5):
		time.sleep(60)
		r = os.system("ping -c 1 -w 1 192.168.1.101")
		if r != 0:
			i += 1
		else:
			left = False

	if left:
		deviceHandler.setLightState(1, "off")
		deviceHandler.setLightState(2, "off")
		deviceHandler.setLightState(3, "off")
		deviceHandler.setLightState(4, "off")
		requests.get(url5)

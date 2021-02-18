import requests
import json
import os
import time
from utils import deviceHandler

"""
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
"""
if not deviceHandler.getPhoneState(5):
	deviceHandler.setLightState(1, "off")
	deviceHandler.setLightState(2, "off")
	deviceHandler.setLightState(3, "off")
	deviceHandler.setLightState(4, "off")
	deviceHandler.setPlugState(0, "off")

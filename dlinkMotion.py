#!python3
from pyW215 import SmartPlug, ON, OFF
import os
import time
import requests

x = SmartPlug('192.168.1.123', '494763')
#x = SmartPlug('192.168.0.28', '956258')

last = int(x.state)
while True:
	#print(x.state)
	now = int(x.state)
	if now > last:
		#print('MOTION!!!')
		requests.get('http://192.168.1.100:6969/lights/4/on')
		last = now
	if time.time() > last + 60:
		requests.get('http://192.168.1.100:6969/lights/4/off')

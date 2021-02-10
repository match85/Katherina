#!python3
from utils import deviceHandler
import time
import requests



last = deviceHandler.getMotionState()

while True:
	now = deviceHandler.getMotionState()
	if now > last:
		print("Motion")
		requests.get('http://192.168.1.100:6969/lights/4/on')
		last = now
	if time.time() > last + 60:
		print("off")
		requests.get('http://192.168.1.100:6969/lights/4/off')

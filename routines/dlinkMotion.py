#!python3
from utils import deviceHandler
import time

last = deviceHandler.getMotionState()

while True:
	now = deviceHandler.getMotionState()
	if now > last:
		#print("Motion")
		deviceHandler.setLightState(4, "on")
		last = now
	if time.time() > last + 60:
		#print("off")
		deviceHandler.setLightState(4, "off")

#python3
import sys
import json
import miio.viomivacuum

sys.path.append("..")
import time
import datetime
from config_data import deviceInfo
from utils import deviceHandler
from utils import routineHandler
from config_data import routineInfo
from alexa_client import AlexaClient
from utils import statusHandler
from miio import viomivacuum

vac = viomivacuum.ViomiVacuum("192.168.1.185", "4c3852586a715070644c78664c426a6d")
#vac.set_edge(miio.viomivacuum.ViomiEdgeState.On)
'''
print("Start 1")
vac.move(viomivacuum.ViomiMovementDirection.Forward, 20)
time.sleep(30)
print("Finish 1")
print("start 2")
vac.move(viomivacuum.ViomiMovementDirection.Left, 1)
time.sleep(10)
print("finish 2")
print("start 3")
vac.move(viomivacuum.ViomiMovementDirection.Forward, 5)
time.sleep(10)
print("finish 3")
time.sleep(20)
print("go home")


print("Send to the hallway")
vac.start_with_room(rooms={"Hallway"})

print("Sleep")
time.sleep(80)
print("Pausing")
vac.pause()
print("Sleep")
time.sleep(30)
print("Send to home")
vac.home()
'''

statusHandler.setPhoneLast(time.time())
time.sleep(10)
print(int(time.time() - statusHandler.getPhoneLast()))
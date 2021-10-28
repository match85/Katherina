import platform
import subprocess
import time
from config_data import deviceInfo
from utils import statusHandler


def ping():
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    param2 = '-w' if platform.system().lower() == 'windows' else '-W'
    command = ['ping', param, '1', param2, '1', deviceInfo.getPhoneIp()]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    response = str(out).lower().find("ttl")
    if response == -1:
        return False
    else:
        return True


storedState = statusHandler.getPhoneState()
currentState = ping()

if not currentState:
    i = 0
    while (not currentState) and (i < 5):
        time.sleep(3)
        currentState = ping()
        i += 1

if currentState != storedState:
    statusHandler.setPhoneState(currentState)
    statusHandler.setPhoneLast(time.time())

#python3
import sys
sys.path.append("..")

from config_data import deviceInfo
from utils import deviceHandler
from miio import Vacuum

vac = Vacuum("192.168.1.185", "4c3852586a715070644c78664c426a6d")
print(str(vac.send_handshake()))
vac.start()
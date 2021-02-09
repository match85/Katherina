import requests
import json
import os
import time

url1 = "http://192.168.1.110/api/XlAMIoJxhvTwYMQiefuXtjQfnfDVG4tEMOhnHVtv/lights/1/state"
url2 = "http://192.168.1.110/api/XlAMIoJxhvTwYMQiefuXtjQfnfDVG4tEMOhnHVtv/lights/2/state"
url3 = "http://192.168.1.110/api/XlAMIoJxhvTwYMQiefuXtjQfnfDVG4tEMOhnHVtv/lights/3/state"
url4 = "http://192.168.1.110/api/XlAMIoJxhvTwYMQiefuXtjQfnfDVG4tEMOhnHVtv/lights/4/state"
url5 = "http://192.168.1.100:6969/plugs/0/off"

data_on = {"on":True}
data_off = {"on":False}

r = os.system("ping -c 1 -W 1 192.168.1.101")

if r != 0:
	i = 0
	left = True
	#time.sleep(120)
	while left and (i < 5):
		time.sleep(60)
		r = os.system("ping -c 1 -W 1 192.168.1.101")
		if r != 0:
			i += 1
		else:
			left = False

	if left:
		requests.put(url1, json.dumps(data_off), timeout=5)
		requests.put(url2, json.dumps(data_off), timeout=5)
		requests.put(url3, json.dumps(data_off), timeout=5)
		requests.put(url4, json.dumps(data_off), timeout=5)
		requests.get(url5)

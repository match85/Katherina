#python3
import sys
#sys.path.append("../..")
from flask import Flask
import requests
from utils import deviceHandler
from flask import request

#sp = [SmartPlug('192.168.1.120', '956258'), SmartPlug('192.168.1.121', '222595')]

app = Flask(__name__)

@app.route('/')
def index():
	return 'hello world'

@app.route('/lights/<id>/<switch>')
def switchLight(id, switch):
	deviceHandler.setLightState(id, switch)
	return 'OK'

@app.route('/lights/<id>/state')
def switchState(id):
	return str(deviceHandler.getLightState(id))

@app.route('/plugs/<int:id>/<switch>')
def switchPlug(id, switch):
	deviceHandler.setPlugState(id, switch)
	return 'OK'

@app.route('/plugs/<int:id>/state')
def plugState(id):
	return str(deviceHandler.getPlugState(id))

@app.route('/sensors/<id>/<category>/<element>')
def sensorState(id, category, element):
	url = "http://192.168.1.110/api/XlAMIoJxhvTwYMQiefuXtjQfnfDVG4tEMOhnHVtv/sensors/" + id
	r = requests.get(url)
	data = r.json()
	return str(data[category][element])

"""
server_address = ('192.168.1.130', 6970)
@app.route('/roomba/<command>')
def setRoomba(command):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		print('Connecting')
		sock.connect(server_address)
		print('Sending')
		sock.sendall(command)
	finally:
		print('Closing')
		sock.close()
		return 'OK'
"""

@app.route('/test')
def getParams():
	param1 = request.args.get('temp')
	return str(param1)

@app.route('/ht/report')
def getTemp():
	temp = request.args.get('temp')
	hum = request.args.get('hum')
	deviceHandler.setCurrentTemperature(1, temp)
	deviceHandler.setCurrentHumidity(1, hum)
	return temp

if __name__ == '__main__':
	app.run(debug=True, port=6969, host='0.0.0.0')
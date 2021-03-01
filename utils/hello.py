#python3
import sys
sys.path.append("..")
from flask import Flask
import requests
from utils import deviceHandler
from utils import monitor
from flask import request
from config_data import init_config
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)

app = Flask(__name__)

hubUrl = "http://" + init_config.getPhilipsIp() + "/api/" + init_config.getPhilipsAuth()

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
	url = hubUrl + "/sensors/" + id
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
	logging.info("Updating HT data:")
	logging.info("New current temperature: " + str(temp))
	logging.info("New current humidity: " + str(hum))
	return temp

@app.route('/monitor')
def statusMonitor():
	response = monitor.getMonitor()
	return response

if __name__ == '__main__':
	app.run(debug=False, port=6969, host='0.0.0.0')
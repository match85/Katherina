# python3
import datetime
import sys

sys.path.append("..")
from flask import Flask, jsonify, Response
import requests
from utils import deviceHandler
from utils import monitor
from utils import statusHandler
from flask import request
import logging
from config_data import routineInfo
from config_data import deviceInfo
import importlib

app = Flask(__name__)
app.logger.setLevel(logging.ERROR)

hubUrl = "http://" + deviceInfo.getPhilipsData("hub", "1", "ip") + "/api/" + deviceInfo.getPhilipsData("hub", "1", "auth")


@app.route('/')
def index():
    return 'hello world'


@app.route('/lights/<id>/<switch>')
def switchLight(id, switch):
    if switch == 'on':
        deviceHandler.setLightState(int(id), True)
    else:
        deviceHandler.setLightState(int(id), False)
    return 'OK'


@app.route('/lights/<id>/state')
def switchState(id):
    return str(deviceHandler.getLightState(int(id)))


@app.route('/lights/<id>/brightness/<level>')
def SetBrightness(id, level):
    deviceHandler.setLightBrightness(id, level)
    return "OK"


@app.route('/plugs/<int:id>/<switch>')
def switchPlug(id, switch):
    deviceHandler.setPlugState(id, switch)
    return 'OK'


@app.route('/plugs/<int:id>/state')
def plugState(id):
    return str(deviceHandler.getPlugState(id))

#Refactor this
@app.route('/sensors/<id>/<category>/<element>')
def sensorState(id, category, element):
    url = hubUrl + "/sensors/" + id
    r = requests.get(url)
    data = r.json()
    return str(data[category][element])

@app.route('/sensors/motion/<id>')
def motionState(id):
    importlib.reload(deviceInfo)
    return str(deviceInfo.getPhilipsData("motion", id, "state"))

@app.route('/test')
def getParams():
    param1 = request.args.get('temp')
    return str(param1)


@app.route('/ht/report')
def getTemp():

    temp = request.args.get('temp')
    hum = request.args.get('hum')
    statusHandler.setCurrentTemp(1, temp)
    statusHandler.setCurrentHum(1, hum)
    logging.info("Updating HT data:")
    logging.info("New current temperature: " + str(temp))
    logging.info("New current humidity: " + str(hum))
    return temp


@app.route('/monitor')
def statusMonitor():
    response = monitor.getMonitor()
    return response

@app.route('/routine')
def setRoutine():
    routine = request.args.get('routine')
    item = request.args.get('item')
    value = request.args.get('value')
    routineInfo.setRoutineData(routine, item, value)
    response = routineInfo.getRoutineData(routine, item)
    return response

@app.route('/currentTemp')
def currentTemp():
    return statusHandler.getCurrentTemp(1)

@app.route('/minTemp')
def minTemp():
    return routineInfo.getRoutineData("temp", "min_temp")

@app.route('/maxTemp')
def maxTemp():
    return routineInfo.getRoutineData("temp", "max_temp")

@app.route('/log/<num>')
def log(num):
    with open("../logs/" + str(datetime.date.today()) + ".log", "r") as log_file:
        lines = log_file.readlines()
        return Response(lines[int(num) * -1:], mimetype="text/plain", content_type="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True, port=6969, host='0.0.0.0')

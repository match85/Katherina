from Test import botoTest


def getCurrentTemperature(id):
    r = botoTest.get_data("Temperature", id)
    r2 = r.get("info")
    return float(r2.get("current_temp"))

def getMinTemperature(id):
    r = botoTest.get_data("Temperature", id)
    r2 = r.get("info")
    return float(r2.get("min_temp"))

def getMaxTemperature(id):
    r = botoTest.get_data("Temperature", id)
    r2 = r.get("info")
    return float(r2.get("max_temp"))

def setCurrentTemperature(id, value):
    botoTest.update_data("Temperature", id, "current_temp", value)
    return "OK"

def setMinTemperature(id, value):
    botoTest.update_data("Temperature", id, "min_temp", value)
    return "OK"

def setMaxTemperature(id, value):
    botoTest.update_data("Temperature", id, "max_temp", value)
    return "OK"

def setCurrentHumidity(id, value):
    botoTest.update_data("Humidity", id, "current_hum", value)
    return "OK"

def getCurrentHumidity(id):
    r = botoTest.get_data("Humidity", id)
    r2 = r.get("info")
    return float(r2.get("current_hum"))

def getMinHumidity(id):
    r = botoTest.get_data("Humidity", id)
    r2 = r.get("info")
    return float(r2.get("min_hum"))

def getMaxHumidity(id):
    r = botoTest.get_data("Humidity", id)
    r2 = r.get("info")
    return float(r2.get("max_hum"))
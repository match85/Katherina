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
    min = getMinTemperature(id)
    max = getMaxTemperature(id)
    botoTest.update_data("Temperature", id, value, min, max)
    return "OK"

def setMinTemperature(id, value):
    current = getCurrentTemperature(id)
    max = getMaxTemperature(id)
    botoTest.update_data("Temperature", id, current, value, max)
    return "OK"

def setMaxTemperature(id, value):
    current = getCurrentTemperature(id)
    min = getMinTemperature(id)
    botoTest.update_data("Temperature", id, current, min, value)
    return "OK"
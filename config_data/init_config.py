from configparser import ConfigParser

config = ConfigParser(allow_no_value=True)
config.read("../config_data/config.ini")

#Raspberry config data
def getRpiIp():
    return config["Raspberry"]["ip"]


#Flask config data
def getFlaskIp():
    return config["Flask"]["ip"]

def getPortIp():
    return config["Flask"]["port"]


#Phone config data
def getPhoneIp():
    return config["Phone"]["ip"]


#Philips config data
def getPhilipsIp():
    return config["Philips"]["ip"]

def getPhilipsAuth():
    return config["Philips"]["auth"]


#Dynamo config data
def getDynamoUrl():
    return config["dynamo"]["url"]


#Dlink config data
##Plugs
def getDlinkPlugIp(id):
    return config["DLink"]["plug_ip_" + str(id)]

def getDlinkPlugAuth(id):
    return config["DLink"]["plug_auth_" + str(id)]

##Motion
def getDlinkMotionIp():
    return config["DLink"]["motion_ip"]

def getDlinkMotionAuth():
    return config["DLink"]["motion_auth"]


#TODO
#Shelly config data
##Temperature



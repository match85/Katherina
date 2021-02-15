from configparser import ConfigParser

config = ConfigParser(allow_no_value=True)
#config.read(r"C:\Users\match\PycharmProjects\Katherina\config_data\config.ini")
config.read("../config_data/config.ini")

#Raspberry config_data data
def getRpiIp():
    return config["Raspberry"]["ip"]


#Flask config_data data
def getFlaskIp():
    return config["Flask"]["ip"]

def getPortIp():
    return config["Flask"]["port"]


#Phone config_data data
def getPhoneIp():
    return config["Phone"]["ip"]


#Philips config_data data
def getPhilipsIp():
    return config["Philips"]["ip"]

def getPhilipsAuth():
    return config["Philips"]["auth"]


#Dynamo config_data data
def getDynamoUrl():
    return config["dynamo"]["url"]


#Dlink config_data data
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
#Shelly config_data data
##Temperature



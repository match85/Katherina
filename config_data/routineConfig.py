from configparser import ConfigParser

config = ConfigParser(allow_no_value=True)
config.read("../config_data/routines_config.ini")

def getEnabledState(routine):
    return config[routine]["enabled"]

def setEnabledState(routine, state):
    config[routine]["enabled"] = str(state)
    with open("../config_data/routines_config.ini", "w") as configfile:
        config.write(configfile)
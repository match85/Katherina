#python3
import logging
import sys
import json
import requests

from utils.pyW215 import SmartPlug

sys.path.append("..")
import time
import datetime
from config_data import deviceInfo
from utils import deviceHandler
from utils import routineHandler
from config_data import routineInfo
from alexa_client import AlexaClient
from utils import statusHandler2
import paho.mqtt.client as mqtt
from utils.pyW215 import SmartPlug, ON, OFF

'''

sp = SmartPlug(deviceInfo.getDlinkData("plug", 1, "ip"), deviceInfo.getDlinkData("plug", 1, "auth"))
while True:
    print("Total: " + str(sp.total_consumption) + " Current: " + str(sp.current_consumption))
    time.sleep(10)
#send_magic_packet('24.a2.e1.f3.68.2a', ip_address='192.168.1.178', port=80)
'''

'''
import requests
token = "7345751570:AAF0M9MR4ZuQP7MIJPxo9QZFeiA0Rj9U5Tw"
url = f"https://api.telegram.org/bot{token}"
params = {"chat_id": "7252664238", "text": "Hello World"}
r = requests.get(url + "/sendMessage", params=params)
'''

'''
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, Updater


def message_handler(update, context):
    # Get the message from the update
    message = update.message

    # Print the message to the console
    print(message.text)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("7345751570:AAF0M9MR4ZuQP7MIJPxo9QZFeiA0Rj9U5Tw").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
'''
deviceHandler.setLightState(1, True)

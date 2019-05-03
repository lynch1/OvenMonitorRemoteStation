# Adapted from "simple-test.py" by Tony Dicola under Public Domain License.
# Original available at: 
# https://github.com/adafruit/Adafruit_Python_MCP3008/tree/master/examples
# Modified by Daniel Lynch for Remote Oven Monitoring Station Project
# Remote Oven Monitoring Station Project Github available at:
# https://github.com/lynch1/OvenMonitorRemoteStation

import time
import datetime
import random
import serial
import remotemqttclient as config

measurementFile = open(config.LATEST_MEASUREMENTS, 'w')

sampleTime = datetime.datetime.now()


# Open Serial Connection
sp = serial.Serial(port = "/dev/ttyUSB0", baudrate = 57600, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, timeout = 1)
qmsg  = bytearray("?:3010:00::c2\r", "ascii")
sp.write(qmsg)
line = sp.readline()
# Nice to see what's happening
# print(line)
# Parse the recieved message
#setTemp = line[9:17]
#currentTemp = line[17:24]

tempTemp = line
#setTemp + ", " + currentTemp

messageString = config.REMOTE_STATION_NAME + '~' + config.FEED_1_NAME + '~'
messageString = messageString + str(sampleTime) + '~'
messageString = messageString + str(tempTemp)

measurementFile.write(messageString)

measurementFile.close()

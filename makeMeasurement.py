# Adapted from "simple-test.py" by Tony Dicola under Public Domain License.
# Original available at: 
# https://github.com/adafruit/Adafruit_Python_MCP3008/tree/master/examples
# Modified by Daniel Lynch for Remote Oven Monitoring Station Project
# Remote Oven Monitoring Station Project Github available at:
# https://github.com/lynch1/OvenMonitorRemoteStation

import time
import datetime
import random
import remotemqttclient as config

measurementFile = open(config.LATEST_MEASUREMENTS, 'w')

sampleTime = datetime.datetime.now()

sumValue = 0
# Main program loop.
for i in range(10):
    sumValue = sumValue + random.randrange(10)
    time.sleep(0.5)

sumValue = sumValue / 10

messageString = config.REMOTE_STATION_NAME + '~' + config.FEED_1_NAME + '~'
messageString = messageString + str(sampleTime) + '~'
messageString = messageString + str(sumValue)

measurementFile.write(messageString)

measurementFile.close()
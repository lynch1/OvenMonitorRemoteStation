# Adapted from "simple-test.py" by John Robinson under Public Domain License.
# Original available at:
# https://github.com/johnrbnsn/Adafruit_Python_MAX31856/blob/master/Adafruit_MAX31856/max31856.py# https://github.com/adafruit/Adafruit_Python_MCP3008/tree/master/examples
# Modified by Daniel Lynch for Remote Oven Monitoring Station Project
# Remote Oven Monitoring Station Project Github available at:
# https://github.com/lynch1/OvenMonitorRemoteStation

import logging
import time
import Adafruit_GPIO

# Local Imports
from Adafruit_MAX31856 import MAX31856 as MAX31856

# Raspberry Pi hardware SPI configuration.
SPI_PORT   = 0
SPI_DEVICE = 0
sensor = MAX31856(hardware_spi=Adafruit_GPIO.SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Loop printing measurements every second.
print('Press Ctrl-C to quit.')
while True:
    temp = sensor.read_temp_c()
    internal = sensor.read_internal_temp_c()
    print('Thermocouple Temperature: {0:0.3F}*C'.format(temp))
    print('    Internal Temperature: {0:0.3F}*C'.format(internal))
    time.sleep(1.0)

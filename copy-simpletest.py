# Adapted from "simple-test.py" by Tony Dicola under Public Domain License.
# Original available at: 
# https://github.com/adafruit/Adafruit_Python_MCP3008/tree/master/examples
# Modified by Daniel Lynch for Remote Oven Monitoring Station Project
# Remote Oven Monitoring Station Project Github available at:
# https://github.com/lynch1/OvenMonitorRemoteStation

import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# My Project specific stuff
thermChannel = 7
tempTable = open('temporaryTableOfData.txt', 'a')

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


# print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
# print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
# print('-' * 57)
currentValue = 0
# Main program loop.
for i in range(10):
    # Read all the ADC channel values in a list.
    # values = [0]*8
    # for i in range(8):
        #  # The read_adc function will get the value of the specified channel (0-7).
    currentValue = mcp.read_adc(thermChannel)
    # Print the ADC values.
    # print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    # Pause for half a second.
    tempTable.write('Temp {0:4d} \n'.format(currentValue))
    time.sleep(0.5)

tempTable.close()


import time

# Open the config file for reading 
configFile = open("raspi-remote-mqtt-client.conf", "r")
configList = []
# Iterate through lines
for line in configFile:
    if line[-1] == '\n':
        configList.append(line[:-1])
    else:
        configList.append(line)

configDict = {}
settingName = ''
settingValue =''
for i in range(0,(len(configList) - 1)):
    settingName = ''
    settingValue =''
    delimiterFlag = False
    # pastDelimiterFlag = 0
    for character in configList[i]:
        # Check if it is :
        if(character ==':'):
            delimiterFlag = True
        else:
            if (not(delimiterFlag)):
                settingName = settingName + character
            else:
                settingValue = settingName + character
    configDict[settingName] = settingValue
    delimterFlag = False

# For debugging
# Print list
print("configlist is: \n")
print(configList)
# # Print Dictionary
for key, val in configDict.items():
    print key + " => " + val
print configDict["Feed 1 Name"]
# print("configDict is: \n"
# print(configDict.items())

# # Read in the expected first bit and get the address
# MQTT Broker IP: 18.218.123.57
# address = 
# # Read in the next expected bit and get the port
# MQTT Broker Port: 1883
# # Read in the next expected bit and get the station name
# MQTT Remote Station Name: BlueMOven 
# # Read in the next expected bit and get the number of feeds
# Number of Feeds: 1
# # Read in the next expected bit and get the feed reading for feed 1
# Feed 1 Name: ThermistorReading
# # Read in the next expected bit and get the type of reading for feed 1
# Feed 1 Type: Number

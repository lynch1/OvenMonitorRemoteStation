# This example came from:
# http://www.steves-internet-guide.com/into-mqtt-python-client/

import paho.mqtt.client as paho
import remotemqttclient as config

def on_publish(client,userdata,result):             #create function for callback
    print("Your message was published .\n")
    pass


stationAddress = config.MQTT_BROKER_IP
# Build a topic string
topicName = config.MQTT_REMOTE_STATION_NAME + "/" + config.FEED_1_NAME
# Build a message string
temp = 68
messageData = str(temp) + " degrees" 
client1 = paho.Client(config.MQTT_REMOTE_STATION_NAME)               
client1.on_publish = on_publish                          
client1.connect(config.MQTT_BROKER_IP, config.MQTT_BROKER_PORT)
ret = client1.publish(topicName, messageData)

print ret
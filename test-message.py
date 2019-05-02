# Adapted from examples on PyPI's paho-mqtt library documentation page
# Original available at: 
# https://pypi.org/project/paho-mqtt/
# Modified by Daniel Lynch for Remote Oven Monitoring Station Project
# Remote Oven Monitoring Station Project Github available at:
# https://github.com/lynch1/OvenMonitorRemoteStation

# This is a program to be run on a Raspberry Pi or other Linux machine
# that reads recent measurements from a local .txt and sends them
# as messages to an MQTT topic specified in remotemqttclient.py
# It also should log data locally in a file specified in 
# remotemqttclient.py


import io
import time
import paho.mqtt.client as paho
import remotemqttclient as config

# Call back funciton
def on_publish(client,userdata,result):
    print("Your message was published .\n")
    pass
# Main
def main():
	stationAddress = config.MQTT_BROKER_IP
	# Build a topic string
	topicName = config.MQTT_MESSAGE_TOPIC
	# Build a message string from the info in latest-measurement.txt
	try:
		latestMeas =open(config.FEED_1_LATEST_MEASUREMENT, 'r')
		print("Opened file.")
		reading = latestMeas.read();
		messageData = reading
		# Connect to MQTT broker
		client1 = paho.Client(config.REMOTE_STATION_NAME)               
		client1.on_publish = on_publish                          
		client1.connect(config.MQTT_BROKER_IP, config.MQTT_BROKER_PORT)
		# Publish message and print confirmation
		ret = client1.publish(topicName, messageData)
		print ret
		# Close file
		latestMeas.close();
	except IOError:
		print("Could not open file. Try again")
	finally:
		print("Exit")


if __name__== "__main__":
	main()
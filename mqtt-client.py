#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import RPi.GPIO as gpio

def gpioSetup():
	#Set in numbering to Broadcom scheme
	gpio.setmode(gpio.BCM)

	#Set GPIO21 (pin 40) as an output pin
	gpio.setup(21, gpio.OUT)

#Ececute when a connection has been established to the MQTT server
def connectionStatus(client, userdata, flags, rc):
	#Subscribe client to a topic
	mqttClient.subscribe("rpi/gpio")

#Execute when a message has been received from the MQTT server
def messageDecoder(client, userdata, msg):
	#Decode message received from topic
	message = msg.payload.decode(encoding='UTF-8')

	#Set GPIO pin 40 HIGH or LOW
	if message == "on":
		gpio.output(21, gpio.HIGH)
		print("LED is ON!")
	elif message == "off":
		gpio.output(21, gpio.LOW)
		print("LED is OFF!")
	else:
		print("Unknown message!")

try:
	# Set up RPI GPIO pins
	gpioSetup()

	#Set client name
	clientName = "raspiw1"

	#Set MQTT server address
	serverAddress = "192.168.11.12"

	#Instantiate Eclipse Paho as mqttClient
	mqttClient = mqtt.Client(clientName)

	#Set calling functions to mqttClient
	mqttClient.on_connect = connectionStatus
	mqttClient.on_message = messageDecoder

	#Connect client to server
	mqttClient.connect(serverAddress)

	#Monitor client activity forever
	mqttClient.loop_forever()

except KeyboardInterrupt:
	mqttClient.disconnect()
	pass
except Exception as e:
	print(e)

finally:
	gpio.output(21, gpio.LOW)
	gpio.cleanup()

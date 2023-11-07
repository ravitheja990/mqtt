# Importing necessary modules
import paho.mqtt.client as mqtt  # Importing the MQTT client module
from random import randrange, uniform  # Importing functions for generating random numbers
import time  # Importing the time module

# Defining the MQTT broker's address
mqttBroker = "mqtt.eclipseprojects.io"

# Creating an MQTT client instance with the identifier "Temperature_Outside"
client = mqtt.Client("Temperature_Outside")

# Connecting the client to the MQTT broker
client.connect(mqttBroker)

# Continuous loop for generating and publishing random temperature data
while True:
    # Generating a random integer between 0 and 9
    randNumber = randrange(10)

    # Publishing the random number to the topic "TEMPERATURE"
    client.publish("TEMPERATURE", randNumber)

    # Printing the information about the published data to the console
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")

    # Adding a 1-second delay before the next iteration
    time.sleep(1)


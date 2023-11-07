# Importing necessary modules
import paho.mqtt.client as mqtt  # Importing the MQTT client module
from random import randrange, uniform  # Importing functions for generating random numbers
import time  # Importing the time module

# Defining the MQTT broker's address
mqttBroker = "mqtt.eclipseprojects.io"

# Creating an MQTT client instance with the identifier "Temperature_Inside"
client = mqtt.Client("Temperature_Inside")

# Connecting the client to the MQTT broker
client.connect(mqttBroker)

# Continuous loop for generating and publishing random temperature data
while True:
    # Generating a random floating point number between 20.0 and 21.0
    randNumber = uniform(20.0, 21.0)

    # Publishing the random number to the topic "TEMPERATURE"
    client.publish("TEMPERATURE", randNumber)

    # Printing the information about the published data to the console
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")

    # Adding a 1-second delay before the next iteration
    time.sleep(1)


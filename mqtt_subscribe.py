# Importing necessary modules
import paho.mqtt.client as mqtt  # Importing the MQTT client module
import time  # Importing the time module

# Defining the callback function to handle incoming messages
def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

# Defining the MQTT broker's address
mqttBroker = "mqtt.eclipseprojects.io"

# Creating an MQTT client instance with the identifier "Smartphone"
client = mqtt.Client("Smartphone")

# Connecting the client to the MQTT broker
client.connect(mqttBroker)

# Starting the background thread for the MQTT client
client.loop_start()

# Subscribing to the "TEMPERATURE" topic
client.subscribe("TEMPERATURE")

# Assigning the on_message callback function to the client
client.on_message = on_message

# Waiting for 30 seconds to receive messages
time.sleep(30)

# Ending the background thread for the MQTT client
client.loop_end()


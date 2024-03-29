'''
This script connects to Wifi with input credentials
Establish the MQTT connection with broker
If the connection is successfull it publishes JSON messages and flashes an led 
'''

import network
import utime
from umqtt import MQTTClient
import ujson

# WiFi Connection Details

SSID = "VISHU_WIFI"
PASSWORD = "123456789"

# MQTT Connection Details

MQTT_BROKER = "192.168.0.103"
BROKER_PORT = 1883
MQTT_TOPIC = "Pseudo/BMP280"
CLIENT_ID = "pico_client"

# JSON message
count = 0
led= machine.Pin('LED', machine.Pin.OUT)


# Function to connect to WiFi

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        pass
    print("Connected to WiFi")
    
# Function to connect to MQTT broker

def connect_to_mqtt():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER)
    client.connect()
    print("Connected to MQTT broker")
    return client

# Function to publish message

def publish_message(client, message):
    client.publish(MQTT_TOPIC, ujson.dumps(message))
    print("Message published")


# Main loop

connect_to_wifi(SSID, PASSWORD)
client = connect_to_mqtt()
    
while True:
        
    Senor_data = {
            
        "Message counter": count,
        "Message": "Sensor node running"
        }
    
    publish_message(client, Sensor_data)
    count = count + 1
    led.value(1)
    utime.sleep(1)
    led.value(0)
    utime.sleep(9)  # Send message every 10 seconds
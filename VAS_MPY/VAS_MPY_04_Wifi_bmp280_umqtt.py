'''
This script connects to Wifi with input credentials
Establish the MQTT connection with broker
If the connection is successfull it publishes JSON messages and flashes an led 
'''

from machine import I2C, Pin
from time import sleep
import network
import utime
import ujson
from umqtt import MQTTClient
from bmp280 import *

# WiFi Connection Details

SSID = "VISHU_WIFI"
PASSWORD = "123456789"

# MQTT Connection Details

MQTT_BROKER = "192.168.0.103"
BROKER_PORT = 1883
MQTT_TOPIC = "Pseudo/BMP280"
CLIENT_ID = "pico_client"


# General variable declaraion
Polling_interval = 10
label = 1               # label for CSV headers
count = 0               # Message counter


# Pin assignment 

led = Pin("LED", Pin.OUT)
Pin_SDA = Pin(14)
Pin_SCL = Pin(15)

# Creating i2c object

i2c_bus = I2C(1, scl = Pin_SCL, sda = Pin_SDA, freq = 40000)
scan_result = I2C.scan(i2c_bus)
print(scan_result)

# BMP object Settings
bmp_object = BMP280(i2c_bus, addr = 0x76, use_case = BMP280_CASE_INDOOR)


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


# Function to read sensor data
    
# Function to publish message

def publish_message(client, message):
    client.publish(MQTT_TOPIC, ujson.dumps(message))
    print("Message published")


# Main loop

connect_to_wifi(SSID, PASSWORD)
client = connect_to_mqtt()
    
while True:
    
    temperature = bmp_object.temperature
    pressure = bmp_object.pressure
        
    Sensor_data = {
            
        "Message counter": count,
        "Temperature_C": temperature,
        "Pressure" : pressure
        }
    
    publish_message(client, Sensor_data)
    print('Sensor data:', Sensor_data)
    count = count + 1
    led.value(1)
    utime.sleep(1)
    led.value(0)
    utime.sleep(9)  # Send message every 10 seconds
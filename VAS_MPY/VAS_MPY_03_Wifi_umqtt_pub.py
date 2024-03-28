'''
This script tries to connects to Wifi with input credentials
checks WLAN connection status and prints the IP address
Tries establish the MQTT connection with broker
If the connection is successfull it publishes JSON messages and flashes an led
    
'''

# Libraries and required modules
import machine
import network
from time import sleep
import utime
from umqtt import MQTTClient

led= machine.Pin('LED', machine.Pin.OUT)

# Wifi Connection details (Give your wifi credentials here)

SSID = "VISHU_WIFI"
PASSWORD = "123456789"

# MQTT Connection details

MQTT_BROKER = "192.168.0.103"
BROKER_PORT = 1883
MQTT_TOPIC = "Pseudo/BMP280"

interval = 5
count = 0

# ---------- WiFi Connection ------------

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

if wlan.status() != 3:
    print('Connection failed....')
else:
    print('WLAN Connection status:', wlan.isconnected())
    print('WLAN Staus code: ', wlan.status())
    print('IP: ', wlan.ifconfig()[0])
    
    # Led flashing if WiFi is connected
    
while wlan.isconnected() == False:
     print('Reconnecting to WLAN...')
     sleep(10)

#----- Establish MQTT Connection
     
client = MQTTClient("pico_client", MQTT_BROKER)
client.connect()
print("Connected to MQTT Broker")
     
#--------Publishing to broker
  
while True:
     
    JSON_count = {
    
    "Message Nr" : count,
    "Message"    : "Pico working"
    }
    
    client.publish(b"MQTT_TOPIC", b"JSON_count")
    print("Publish successful", JSON_count)
    count = count + 1
    led.value(1)
    sleep(2)
    led.value(0)
    sleep(3)
    

   



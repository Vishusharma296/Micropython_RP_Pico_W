''' This script tries to 
    connects to Wifi with input credentials
    checks WLAN connection status
    and prints the IP address
    
'''

# Libraries and required modules
import machine
import network
from time import sleep

led= machine.Pin('LED', machine.Pin.OUT)

# Connection details (Give your wifi credentials here)

SSID = '....'               # enter your wifi name
password = '....'  # enter the wifi password

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, password)

if wlan.status() != 3:
    print('Connection failed....')
else:
    print('WLAN Connection status:', wlan.isconnected())
    print('WLAN Staus code: ', wlan.status())
    print('IP: ', wlan.ifconfig()[0])

while wlan.isconnected() == False:
     print('Reconnecting to WLAN...')
     sleep(10)
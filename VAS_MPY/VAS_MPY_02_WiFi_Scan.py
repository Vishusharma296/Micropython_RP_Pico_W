""" Micro Python Script for Raspberry Pi PicoW
    
    ###Program Description:
    
    1) Scan for WiFi
    2) Print SSID, RSSI, encryption type every 30 seconds
    3) Log this data via USB to connected local computer/Pico's memory as CSV file

"""
# Libraries and modules:

import os
import machine
import network
import time


# Connect to WiFi

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# Open UART connection to computer
uart = machine.UART(0, 115200)


# General variable declaraion
Polling_frequency = 60

#log_dir = "F:\MxxxCodes\MPY_Sandbox"
log_file_name = "VAS_01_wifi_data.csv"

# Scan for Wi-Fi networks

def scan_wifi():
    networks = wifi.scan()
    for network in networks:
        ssid = network[0].decode('utf-8')
        rssi = network[3]
        print("SSID: {}, RSSI: {}".format(ssid, rssi))
        
        # Log data to CSV file
        
        #log_file_path = os.path.join(log_dir, log_file_name)
        with open(log_file_name, 'a') as f:
            f.write('{},{}\n'.format(ssid, rssi))
        
        # Send data over UART to computer
        uart.write('{},{}\n'.format(ssid, rssi))
        
        
        # Main loop
while True:
  
    scan_wifi()
    time.sleep(Polling_frequency)

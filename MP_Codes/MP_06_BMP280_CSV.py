"""
This test script reads the external temperature-pressure sensor BMP280 using Pi Pico W
Before reading the sensor values it also scans the devices connected to PiCo via I2C
but does not print the I2C slave address.
This script can record the sensor data in CSV file when connected to USB using PuTTy 

Important data related to BMP280:

• Connects using I2C or SPI. 
• Senses Temperature, pressure and altitude
• I2C address of BMP 280 in hex = 0x76
• Sensor gives temperature in Celsius and pressure in pascal
• Requires driver/external sensor libraray for BMP280.
• See:  https://github.com/dafvid/micropython-bmp280
• Multiple use cases and oversampling possible for BMP280. For Ex:
• Use Cases     :    BMP280_CASE_WEATHER, BMP280_CASE_HANDHELD_LOW, BMP280_CASE_INDOOR
• OverSampling  :    BMP280_OS_LOW, BMP280_OS_STANDARD
• Power Mode    :    BMP_POWER_NORMAL, BMP_POWER_SLEEP
• Possible to change temperature and pressure oversmapling, IIR Filter settings, Power modes
"""


# Libraries

from machine import I2C, Pin
from time import sleep
from bmp280 import *


# Pin assignment and creating i2c object

Pin_led = Pin("LED", Pin.OUT)
Pin_SDA = Pin(14)
Pin_SCL = Pin(15)

i2c_bus = I2C(1, scl = Pin_SCL, sda = Pin_SDA, freq = 40000)

# I2C Scan

scan_result = I2C.scan(i2c_bus)

# BMP object Settings
bmp_object = BMP280(i2c_bus, addr = 0x76, use_case = BMP280_CASE_INDOOR)


# General variable declaraion
Polling_frequency = 10
label = 1

while True:
    
    temperature = bmp_object.temperature
    pressure = bmp_object.pressure
    
    
# Printing and Visualization
    
    
    while label == 1:
        
        Headers = "Temperature_C, Pressure_Pascal"
        print(Headers)
        label = 0
        
    print(temperature, pressure, sep = ',')
    sleep(Polling_frequency)
    
    
   
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
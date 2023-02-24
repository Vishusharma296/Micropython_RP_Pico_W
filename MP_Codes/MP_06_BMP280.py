"""
This test script reads the external temperature-pressure sensonor BMP280 of Pi Pico W

Important data related to BMP280:

• Connects using I2C or SPI. 
• Senses Temperature, pressure and altitude
• I2C address of BMP 280 in hex = 0x76
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
print("I2C scan result : ", scan_result)

if scan_result != []:
    print(" I2C connection successfull ")
else:
    print("No devices connected via I2C found !!!")


# BMP object Settings
bmp_object = BMP280(i2c_bus, addr = 0x76, use_case = BMP280_CASE_INDOOR)


while True:
    
    temperature = bmp_object.temperature
    pressure = bmp_object.pressure
    
    print("Temperature: {} ".format(temperature))
    print("Pressure: {} ".format(pressure))
    print("\n")
    sleep(2)
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
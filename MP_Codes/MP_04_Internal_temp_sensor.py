"""
This test script reads the internal temperature data of Pi Pico W

Important data related to ADC:

• Fifth ADC channel is ADC(4) and is connected to internal temperature sensor. 
• Temperature voltage curve slope for Pico W = -1.721mV/°C
• 12 bit ADC can be scaled to 16 bit (65535 values between 0 and 3.3 V)
• ADC clock 48 MHz
• Sampling rate = 500 kHz ( Each Sample takes 96 clock cycles)
• Sampling time = 2e-6 seconds
• Voltage of Biased bipolar diode at 300K (27°C) = 0.0706V 


"""


# Libraries

from machine import ADC, Pin
import time


# Pin assignment
led = Pin("LED", Pin.OUT)
adc = machine.ADC(4)


# Variable Assignment

Slope_TV = 1.721e-3
Con_factor = 3.3/(65535)

while True:
    
    ADC_val = adc.read_u16()
    V = ADC_val * Con_factor  # ADC Voltage at sensor
    temp_C = 27.0 - (V- 0.706)/(Slope_TV)
    led.value(1)
    print("ADC Value: {} ".format(ADC_val))
    print("Voltage: {} ".format(V))
    print("Temperature: {} ".format(temp_C))
    print("\n")
    time.sleep_ms(3000)
    led.value(0)
    time.sleep_ms(2000)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
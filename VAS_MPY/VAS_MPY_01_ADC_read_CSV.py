""" Micro Python Script for Raspberry Pi PicoW
    
    ###Program Description:
    
    1) To read the analog signal from adc capable pin
    2) To print the value of analog signal from every second n times

"""

# Libraries and modules

import machine
import time

# Set up ADC on Pin 26 and 27
adc_0 = machine.ADC(0)   # Pin 26
adc_1 = machine.ADC(1)   # Pin 27


# Print the value of the analog signal every second for 10 times

Polling_frequency = 1
label = 1


# Initial startup
time.sleep(5)

while True:
    
    ADC0_val = adc_0.read_u16()
    ADC1_val = adc_1.read_u16()
    
    
    while label == 1:
        
        Headers = "ADC_0, ADC_1"
        print(Headers)
        label = 0
    
    print(ADC0_val, ADC1_val, sep =',' )
    
    time.sleep(Polling_frequency)
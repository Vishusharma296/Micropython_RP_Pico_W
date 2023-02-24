# This is a test script to blink external LEDs

import machine
import utime

Led_red = machine.Pin(15, machine.Pin.OUT)


while True:
    
    
    Led_red.value(0)
    print("LED OFF")
    utime.sleep(5)       # Sleep for 5 seconds
    Led_red.value(1)
    print("LED ON")
    utime.sleep(5)
    
    
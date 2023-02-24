# Test script to blink LEDs with buttons using debouncing

from machine import Pin
import time


# Pin assignment
Pin_button = Pin(15, Pin.IN, Pin.PULL_UP)
led_onboard = Pin("LED", Pin.OUT)


# variable assignment
counter = 0
debounce_time = 0  # Debounce time in ms 

while True:
    if ((Pin_button.value() is 0) and (time.ticks_ms()-debounce_time) > 300) : 
        counter+=1
        debounce_time=time.ticks_ms()
        print("Button Pressed")
        led_onboard.value(1)
        print("Count={}".format(counter))
        led_onboard.value(0)
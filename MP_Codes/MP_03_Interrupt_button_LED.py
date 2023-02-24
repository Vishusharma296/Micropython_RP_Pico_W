"""
This test script toggles onboard LED on Pi Pico W with button press
using debouncing and callback functions

"""
# Libraries

from machine import Pin
import time

 j  # Pin assignment

pin_button = Pin(15, Pin.IN, Pin.PULL_UP)  # Pin attached to external button
led = Pin("LED", Pin.OUT)                  # Onboard LED on Pi Pico W

# Variable assignment

interrupt_indicator = 0
time_debounce = 0
counter = 0

# Interrupt Service Routine / Callback Function

def ISR_button(pin_button):
    global interrupt_indicator
    global time_debounce
    
    if(time.ticks_ms()-time_debounce) > 300:
        interrupt_indicator = 1
        time_debounce = time.ticks_ms()
        
# Interrupt request handler

pin_button.irq(trigger = Pin.IRQ_FALLING, handler = ISR_button)

while True:
    if interrupt_indicator == 1:
        interrupt_indicator = 0
        counter+=1
        print("Button Pressed")
        print("Count={}".format(counter))
        led.toggle()


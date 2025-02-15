from machine import *
from time import *

pin0 = Pin(1, Pin.OUT)
pin1 = Pin(2, Pin.OUT)
pin2 = Pin(0, Pin.OUT) 

pin1.toggle()

def flash(i):
    for i in range(i):
        pin2.toggle()
        pin0.toggle()
        pin1.toggle()

        sleep_ms(100)
        pin2.toggle()

        pin0.toggle()
        pin1.toggle()
        sleep_ms(100)

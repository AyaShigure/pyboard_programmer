from machine import *
from time import *

pin = Pin(25, Pin.OUT)
pin.toggle()

def flash(i):
    for i in range(i):
        pin.toggle()
        sleep(1)
        pin.toggle()
        sleep(1)
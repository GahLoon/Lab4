import RPi.GPIO as GPIO
import time
from time import sleep

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.IN)
    GPIO.setup(24,GPIO.OUT)

def read_slide_switch():
    ret = 0
    if GPIO.input(22) == 1:
        ret = 1
        GPIO.output(24, 1)
        sleep(0.5)
        GPIO.output(24, 1)
        sleep(0.5)

    else:
        for i in range(0,5):
            GPIO.output(24, 1)
            sleep(0.2)
            GPIO.output(24, 0)
            sleep(0.2)

        time.sleep(0.5)
        while(True and GPIO.input(22) == 0):
            GPIO.output(24,0)

    return ret

while(True):
    init()
    read_slide_switch()

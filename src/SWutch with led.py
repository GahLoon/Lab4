from hal import hal_input_switch as switch
import RPi.GPIO as GPIO
from time import sleep

switch.init()
GPIO.setup(24, GPIO.OUT)

def main():
    sw = switch.read_slide_switch()
    if sw == 0:
        GPIO.output(24,1)
        sleep(0.5)
        GPIO.output(24,0)
        sleep(0.5)
    else:
        for i in range(0, 5):
            GPIO.output(24,1)
            sleep(0.2)
            GPIO.output(24,0)
            sleep(0.2)
        while(True and switch.read_slide_switch()==1):
            GPIO.output(24, 0)

while(True):
    main()
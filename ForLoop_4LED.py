#In this code I added on to a simple LED demo from the 42 Electronics project.
#The original code was just to blink all the LEDs at once, however I modified to for
#them to blink one at a time at varrying intervals and then in reverse.
#Finally a cleanup sequence is run to erase any signals sent to the GPIO pins

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pins = [6, 13, 19, 26]
GPIO.setup(pins, GPIO.OUT)

for i in pins:
    GPIO.output(i, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(i, GPIO.LOW)
    
for i in range(0,4):
    GPIO.output(pins, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(pins, GPIO.LOW)
    time.sleep(.5)
    
for i in reversed(pins):
    GPIO.output(i, GPIO.HIGH)
    time.sleep(.25)
    GPIO.output(pins, GPIO.LOW)
    

GPIO.cleanup()
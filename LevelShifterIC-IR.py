import RPi.GPIO as GPIO
import time

rgb = [13,19,26]
red = 13
green = 19
blue = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(rgb, GPIO.OUT)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)

try:
    while True:
        if GPIO.input(21) == False:
            GPIO.output(green, GPIO.LOW)
            GPIO.output(blue, GPIO.LOW)
            GPIO.output(red, GPIO.HIGH)
        elif GPIO.input(20) == False:
            GPIO.output(green, GPIO.LOW)
            GPIO.output(red, GPIO.LOW)
            GPIO.output(blue, GPIO.HIGH)
        else:
            GPIO.output(red, GPIO.LOW)
            GPIO.output(blue, GPIO.LOW)
            GPIO.output(green, GPIO.HIGH)
            time.sleep(.1)

except KeyboardInterrupt:
    GPIO.cleanup()
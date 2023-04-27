import time
import RPi.GPIO as GPIO
import numpy

rgb = [13,19,26]
red = 13
green = 19
blue = 26
trigger = 20
echo = 21
ranges = []

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(rgb, GPIO.OUT)

def range_check():
    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(trigger, False)
    
    while GPIO.input(echo) == False:
        start_timer = time.time()
    
    while GPIO.input(echo) == True:
        stop_timer = time.time()
        
    elapsed_time = stop_timer - start_timer
    distance = (elapsed_time * 34300)/2
    return distance

def average():
    for i in range (0, 3):
        ranges.append(range_check())
        time.sleep(0.06)
    distance = numpy.mean(ranges)
    ranges.clear()
    return distance

try:
    while True:
        distance = average()
        print('%.1f' % distance)
        if distance < 10:
            GPIO.output(green, GPIO.LOW)
            GPIO.output(blue, GPIO.LOW)
            GPIO.output(red, GPIO.HIGH)
        elif 10 <= distance <20:
            GPIO.output(green, GPIO.HIGH)
            GPIO.output(red, GPIO.LOW)
            GPIO.output(blue, GPIO.LOW)
        else:fa
            GPIO.output(red, GPIO.LOW)
            GPIO.output(blue, GPIO.HIGH)
            GPIO.output(green, GPIO.LOW)
            time.sleep(.1)
        time.sleep(.25)
        
except KeyboardInterrupt:
    GPIO.cleanup()
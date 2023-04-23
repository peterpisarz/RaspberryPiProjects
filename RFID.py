#!/usr/bin/env python3

import RPi.GPIO as GPIO
import SimpleMFRC522
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

pwm_26 = GPIO.PWM(26, 70)
pwm_26.start(0)
pwm_19 = GPIO.PWM(19, 70)
pwm_19.start(0)

reader = SimpleMFRC522.SimpleMFRC522()

try:
    while True:
        id, text = reader.read()
        text = text.strip()
        if text == "card":
            print('ACCESS GRANTED')
            pwm_26.ChangeDutyCycle(50)
            time.sleep(0.5)
            pwm_26.ChangeDutyCycle(0)
        else:
            print('ACCESS DENIED')
            pwm_19.ChangeDutyCycle(70)
            time.sleep(0.5)
            pwm_19.ChangeDutyCycle(0)
        time.sleep(.3)
except KeyboardInterrupt:
        GPIO.cleanup()

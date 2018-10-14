# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 16:41:05 2018

@author: test
"""

import RPi.GPIO as GPIO
from time import sleep

ledlist = [23,24]
switch=18

GPIO.setmode(GPIO.BCM)

GPIO.setup (switch, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setwarnings(False)
GPIO.setup(ledlist[0], GPIO.OUT)
GPIO.setup(ledlist[1], GPIO.OUT)

def blink(gpio_number,duration):
    GPIO.output(gpio.number,GPIO.HIGH)
    sleep(duration)
    GPIO.output(gpio.number, GPIO.LOW)
    sleep(duration)
    
try:
    while(True):
        if GPIO.input(switch) == GPIO.HIGH:
            blink(ledlist[1], 1)
        else:
            blink(ledlist[0], 1)
except KeyboardInterrupt:
    GPIO.cleanup()
    

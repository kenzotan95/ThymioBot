import RPi.GPIO as GPIO
from time import sleep

ledlist = (25,24)
switch = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup (switch, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setwarnings(False)
GPIO.setup(ledlist[0], GPIO.OUT)
GPIO.setup(ledlist[1], GPIO.OUT)

def blink(gpio_number,duration):
     GPIO.output(gpio_number,GPIO.HIGH)
     sleep(duration)
     GPIO.output(gpio_number, GPIO.LOW)
     sleep(duration)

try:
    while(True):
         if GPIO.input(switch) == GPIO.HIGH:
            blink(ledlist[1], 1)
            
         else:
            blink(ledlist[0], 1)
            print("here")
except KeyboardInterrupt():
    GPIO.cleanup()

import RPi.GPIO as GPIO
from time import sleep

ledlist = (25,24)
switch = 18

GPIO.setwarnings(False)

def blink(gpio_number,duration):
     GPIO.output(gpio_number,GPIO.HIGH)
     sleep(duration)
     GPIO.output(gpio_number, GPIO.LOW)
     sleep(duration)

GPIO.setmode(GPIO.BCM)

GPIO.setup (switch, GPIO.IN, GPIO.PUD_DOWN)

GPIO.setup(ledlist, GPIO.OUT)
#GPIO.setup(ledlist[1], GPIO.OUT)


try:
    while(True):
        if GPIO.input(switch) == GPIO.HIGH:
            blink(24, 1)
            
        else:
            blink(25, 1)
except KeyboardInterrupt():
    GPIO.cleanup()

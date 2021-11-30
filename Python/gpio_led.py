# Bob Kammauff
# RPi GPIO Pin Introduction
# 11/16/21

# https://raspberrypihq.com/making-a-led-blink-using-the-raspberry-pi-and-python/

import RPi.GPIO as GPIO
from time import sleep

greenPin = 21
redPin = 19

GPIO.setmode(GPIO.BCM) #this sets my pin numbering scheme as
# the BCM numbering scheme

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setup(redPin, GPIO.OUT, initial=GPIO.LOW) #initializes the pin
GPIO.setup(greenPin, GPIO.OUT, initial=GPIO.HIGH)
while True:
	GPIO.output(redPin, GPIO.HIGH) # red on
	GPIO.output(greenPin, GPIO.LOW) # green off
	sleep(1) 
	GPIO.output(redPin, GPIO.LOW) # red off
	GPIO.output(greenPin, GPIO.HIGH) # green on
	sleep(1)

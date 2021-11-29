# Bob Kammauff
# RPi GPIO Pin Introduction
# 11/16/21

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) #this sets my pin numbering scheme as
# the BCM numbering scheme

GPIO.setwarnings(False)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(21, GPIO.OUT, initial=GPIO.HIGH)
while True:
	GPIO.output(19, GPIO.HIGH) 
	GPIO.output(21, GPIO.LOW) 
	sleep(1) 
	GPIO.output(19, GPIO.LOW) 
	GPIO.output(21, GPIO.HIGH)
	sleep(1)

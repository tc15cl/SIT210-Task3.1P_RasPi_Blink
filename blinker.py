#
# Project: RasPi Blink (SIT210-05.1P)
# Description: Blinking LED on Raspberry Pi
# Author: tjcook (214014891)
# Date: 29/03/20

#Import raspberry pi GPIO & time libraries
import RPi.GPIO as GPIO
from time import sleep

#Set pinout mode (BCM or physical)
GPIO.setmode(GPIO.BCM)

#Set pin as output
GPIO.setup(20, GPIO.OUT)

#Blink LED and sleep every 250ms
try:
    while 1:
        GPIO.output(20, GPIO.HIGH)
        sleep(0.25)
        GPIO.output(20, GPIO.LOW)
        sleep(0.25)
except KeyboardInterrupt:
    GPIO.cleanup() #stop and clean when CTRL+C pressed



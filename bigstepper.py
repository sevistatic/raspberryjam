#!/usr/bin/python
import atexit
import RPi.GPIO as GPIO
from time import sleep

#setup GPIO using Board numbering
GPIO.setmode(GPIO.BCM)

#Motor 1
DIR1 = 13
PUL1 = 16
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(PUL1, GPIO.OUT)

GPIO.output(DIR1, GPIO.LOW)
num = 0
while num  < 1000:
	GPIO.output(PUL1, GPIO.HIGH)
	sleep(0.001)	
	GPIO.output(PUL1, GPIO.LOW)	
	num += 1

GPIO.output(DIR1, GPIO.HIGH)
num = 0
while num  < 1000:
	GPIO.output(PUL1, GPIO.HIGH)
	sleep(0.001)	
	GPIO.output(PUL1, GPIO.LOW)	
	num += 1

#Motor 2
DIR2 = 19
PUL2 = 20
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(PUL2, GPIO.OUT)

GPIO.output(DIR2, GPIO.LOW)
num = 0
while num  < 1000:
	GPIO.output(PUL2, GPIO.HIGH)
	sleep(0.001)	
	GPIO.output(PUL2, GPIO.LOW)	
	num += 1

GPIO.output(DIR2, GPIO.HIGH)
num = 0
while num  < 1000:
	GPIO.output(PUL2, GPIO.HIGH)
	sleep(0.001)	
	GPIO.output(PUL2, GPIO.LOW)	
	num += 1

GPIO.cleanup()

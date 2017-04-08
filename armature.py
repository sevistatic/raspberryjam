#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

#RotationMotor
DIR1 = 13
PUL1 = 16

#TiltMotor
DIR2 = 19
PUL2 = 20

class Armature(object):
	def __init__(self, parent=None):
		#setup GPIO using Board numbering
		GPIO.setmode(GPIO.BCM)
	
		GPIO.setup(DIR1, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(PUL1, GPIO.OUT, initial=GPIO.LOW)
		
		GPIO.setup(DIR2, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(PUL2, GPIO.OUT, initial=GPIO.LOW)
		sleep(1)

	def __del__(self):
		GPIO.cleanup()

	def rotateRight(self):
		GPIO.output(DIR1, GPIO.LOW)
		GPIO.output(PUL1, GPIO.HIGH)
		sleep(0.001)
		GPIO.output(PUL1, GPIO.LOW)

	def rotateLeft(self):
		GPIO.output(DIR1, GPIO.HIGH)
		GPIO.output(PUL1, GPIO.HIGH)
		sleep(0.001)
		GPIO.output(PUL1, GPIO.LOW)

	def tiltDown(self):
		GPIO.output(DIR2, GPIO.LOW)
		GPIO.output(PUL2, GPIO.HIGH)
		sleep(0.001)
		GPIO.output(PUL2, GPIO.LOW)

	def tiltUp(self):
		GPIO.output(DIR2, GPIO.HIGH)
		GPIO.output(PUL2, GPIO.HIGH)
		sleep(0.001)
		GPIO.output(PUL2, GPIO.LOW)

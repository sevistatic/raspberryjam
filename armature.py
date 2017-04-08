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

	num = 0

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
#		num = 0
#		while num  < 1000:
		GPIO.output(PUL1, GPIO.HIGH)
		sleep(0.001)
		GPIO.output(PUL1, GPIO.LOW)
#			num += 1
	def rotateLeft(self):
		GPIO.output(DIR1, GPIO.HIGH)
		#num = 0
		#while num  < 1000:
		GPIO.output(PUL1, GPIO.HIGH)
		sleep(0.001)
		GPIO.output(PUL1, GPIO.LOW)
		#	num += 1
	def tiltDown(self):
		GPIO.output(DIR2, GPIO.LOW)
		#num = 0
		#while num  < 1000:
		GPIO.output(PUL2, GPIO.HIGH)
		sleep(0.001)
		GPIO.output(PUL2, GPIO.LOW)
		#	num += 1
	def tiltUp(self):
		GPIO.output(DIR2, GPIO.HIGH)
		#num = 0
		#while num  < 1000:
		GPIO.output(PUL2, GPIO.HIGH)
		sleep(0.001)
		GPIO.output(PUL2, GPIO.LOW)
		#	num += 1

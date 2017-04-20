#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

#GPIO pins for the rotation stepper motor
#DIR is for direction, PUL is for stepping the motor
#A step happens when the motor alternates once between low and high
DIR1 = 13
PUL1 = 16

#GPIO pins for the tilt stepper motor
DIR2 = 19
PUL2 = 20

#setup GPIO using BCM numbering
#(the values written on the Raspberry Pi 3)
GPIO.setmode(GPIO.BCM)

class Armature(object):
	def __init__(self, parent=None):
	
		GPIO.setup(DIR1, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(PUL1, GPIO.OUT, initial=GPIO.LOW)
		
		GPIO.setup(DIR2, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(PUL2, GPIO.OUT, initial=GPIO.LOW)
	
		#Gives the motors a moment to gain power
		#without this, the first command can lag quite a bit
		sleep(1)

	#Cleanup the GPIO pins used when the application closes
	def __del__(self):
		GPIO.cleanup()

	def rotateRight(self):
		#Set the direction of the motor
		GPIO.output(DIR1, GPIO.LOW)
		self.step(PUL1)

	def rotateLeft(self):
		#Set the direction of the motor
		GPIO.output(DIR1, GPIO.HIGH)
		self.step(PUL1)

	def tiltDown(self):
		#Set the direction of the motor
		GPIO.output(DIR2, GPIO.LOW)
		self.step(PUL2)

	def tiltUp(self):
		#Set the direction of the motor
		GPIO.output(DIR2, GPIO.HIGH)
		self.step(PUL2)

	def step(self,motor):
		#Step the motor
		GPIO.output(motor, GPIO.HIGH)
		sleep(0.001)
		GPIO.output(motor, GPIO.LOW)

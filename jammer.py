#!/usr/bin/python
import RPi.GPIO as GPIO

#GPIO Pin used for the jammer
JAMMER = 21

class Jammer(object):
	def __init__(self):
		#setup GPIO using BCM numbering system
		#(the value written on the Raspberry Pi)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(JAMMER, GPIO.OUT, initial=GPIO.LOW)

	#Reset GPIO pins used when application closes
	def __del__(self):
		GPIO.cleanup()

	def start(self):
		GPIO.output(JAMMER, GPIO.HIGH)
	def stop(self):
		GPIO.output(JAMMER, GPIO.LOW)


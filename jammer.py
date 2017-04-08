#!/usr/bin/python
import RPi.GPIO as GPIO

JAMMER = 21

class Jammer(object):
	def __init__(self):
		#setup GPIO using Board numbering
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(JAMMER, GPIO.OUT, initial=GPIO.LOW)

	def __del__(self):
		GPIO.cleanup()
	def start(self):
		GPIO.output(JAMMER, GPIO.HIGH)
	def stop(self):
		GPIO.output(JAMMER, GPIO.LOW)


#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
from evdev import InputDevice, categorize, ecodes
import time
import atexit
import threading
import random
import RPi.GPIO as GPIO

#setup GPIO using Board numbering
GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

gamepad = InputDevice('/dev/input/event0')
mh = Adafruit_MotorHAT()

st1 = threading.Thread()
st2 = threading.Thread()

def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

rotationMotor = mh.getStepper(50, 1)
tiltMotor = mh.getStepper(50, 2)

def rotateGross(value, center_pos, motor):
	motor.setSpeed(60)
	dir = "NONE"
	if value < (center_pos - 50):
		dir = Adafruit_MotorHAT.FORWARD
	elif value >= (center_pos - 50) and value <= (center_pos + 50):
		return "NONE"
	else:
		dir = Adafruit_MotorHAT.BACKWARD
	return [1, dir, Adafruit_MotorHAT.DOUBLE]		

def rotateFine(value, center_pos, motor):
	motor.setSpeed(60)
	dir = "NONE"
	if value < (center_pos - 25):
		dir = Adafruit_MotorHAT.FORWARD
	elif value >= (center_pos - 25) and value <= (center_pos + 25):
		return "NONE"
	else:
		dir = Adafruit_MotorHAT.BACKWARD
	return [1, dir, Adafruit_MotorHAT.DOUBLE]

def tilt(value, center_pos, motor):
	motor.setSpeed(60)
	dir = "NONE"
	if value < (center_pos - 50):
		dir = Adafruit_MotorHAT.FORWARD
	elif value >= (center_pos - 50) and value <= (center_pos + 50):
		return "NONE"
	else:
		dir = Adafruit_MotorHAT.BACKWARD
	return [1, dir, Adafruit_MotorHAT.DOUBLE]

rotationCommand = "NONE"
tiltCommand = "NONE"
while True:
	GPIO.output(21,1)
	GPIO.output(20,1)

#	event = gamepad.read_one()
#	if event != None and event.type == ecodes.EV_ABS:
#		event = categorize(event).event
#		if event.code == 5:
#			rotationCommand = rotateFine(event.value, 256, rotationMotor)
#		elif event.code == 1:
#			tiltCommand = tilt(event.value, 512, tiltMotor)
#		elif event.code == 0:
#			rotationCommand = rotateGross(event.value, 512, rotationMotor)
#		else:
#			rotationCommand = "NONE"
#			tiltCommand = "NONE"
#	if rotationCommand != "NONE":
#		numSteps = rotationCommand[0]
#		direction = rotationCommand[1]
#		stepType = rotationCommand[2]
#		if direction is Adafruit.MotorHAT.FORWARD:
#			GPIO.output(19, 1)
#		else:
#			GPIO.output(19, 0)
		#rotationMotor.step(numSteps, direction, stepType)
#		GPIO.output(16, 1)
#	else:
#		GPIO.output(16, 0)
#	if tiltCommand != "NONE":
#		numSteps = tiltCommand[0]
#		direction = tiltCommand[1]
#		stepType = tiltCommand[2]
#		if direction is Adafruit.MotorHAT.FORWARD:
#			GPIO.output(21, 1)
#		else:
#			GPIO.output(21, 0)
#		GPIO.output(20, 1)
		#tiltMotor.step(numSteps, direction, stepType)
#	else:
#		GPIO.output(20,0)

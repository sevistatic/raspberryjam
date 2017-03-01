#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
from evdev import InputDevice, categorize, ecodes
import time
import atexit
import threading
import random

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
	if value < (center_pos - 50):
		dir = Adafruit_MotorHAT.FORWARD
		motor.step(1, dir, Adafruit_MotorHAT.DOUBLE)
        	print("Coarse Rotate Left")
	elif value >= (center_pos - 50) and value <= (center_pos + 50):
		print("No Coarse Rotation")
        else:
		dir = Adafruit_MotorHAT.BACKWARD
		motor.step(1, dir, Adafruit_MotorHAT.DOUBLE)
		print("Coarse Rotate Right")
#	print("Z_AXIS EVENT - VAL: {}".format(keyevent.event.value))		

def rotateFine(value, center_pos, motor):
	motor.setSpeed(60)
	if value < (center_pos - 25):
		dir = Adafruit_MotorHAT.FORWARD
		motor.step(1, dir, Adafruit_MotorHAT.DOUBLE)
		print("Fine Rotate Left")
	elif value >= (center_pos - 25) and value <= (center_pos + 25):
		print("No Fine Rotation")
	else:
		dir = Adafruit_MotorHAT.BACKWARD
		motor.step(1, dir, Adafruit_MotorHAT.DOUBLE)
		print("Fine Rotate Right")
#	print("Y_AXIS EVENT - VAL: {}".format(keyevent.event.value))

def tilt(value, center_pos, motor):
	motor.setSpeed(60)
	if value < (center_pos - 50):
		dir = Adafruit_MotorHAT.FORWARD
		motor.step(1, dir, Adafruit_MotorHAT.DOUBLE)
        	print("Tilt Downward")
	elif value <= (center_pos - 50) and value >= (center_pos + 50):
		print("No Rotation")
        else:
		dir = Adafruit_MotorHAT.BACKWARD
		motor.step(1, dir, Adafruit_MotorHAT.DOUBLE)
		print("Tilt Upward")
#	print("X_AXIS EVENT - VAL: {}".format(keyevent.event.value))

for event in gamepad.read_loop():
	if event.type == ecodes.EV_ABS:
		event = categorize(event).event
		if event.code == 5:
			rotateFine(event.value, 256, rotationMotor)
		elif event.code == 1:
			tilt(event.value, 512, tiltMotor)
		elif event.code == 0:
			rotateGross(event.value, 512, rotationMotor)

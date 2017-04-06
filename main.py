#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
from evdev import InputDevice, categorize, ecodes
import time
import atexit
import threading
import random

from PyQt5 import QtGui, QtCore, QtWidgets
import numpy as np
import cv2

import sys
sys.path.append('/usr/local/lib/python3.4/site-packages')

import mainwindow

mh = Adafruit_MotorHAT()

class RaspberryJam(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):

	def __init__(self, parent=None):
		super(RaspberryJam, self).__init__(parent)
		self.setupUi(self)
		layout = QtWidgets.QHBoxLayout(self.cameraFrame)

	def paintEvent(self, QPaintEvent):
		painter = QtGui.QPainter()
		painter.begin(self.cameraFrame)
		#while(cap.isOpened()):
		ret, frame = cap.read()
		height, width, bytevalue = frame.shape
		mQImage = QtGui.QImage(frame, height, width, bytevalue, QtGui.QImage.Format_RGB888)
		if ret:
			painter.drawImage(0, 0, mQImage)
			#layout.addWidget(image)
			#cv2.imshow('frame', frame)
#		if cv2.waitKey(1) & 0xFF == ord('q'):
		#	break
		painter.end()

cap = cv2.VideoCapture(0)

def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

def rotateGross(value, center_pos, motor):
	motor.setSpeed(60)
	dir = "NONE"
	if value < (center_pos - 50):
		dir = Adafruit_MotorHAT.FORWARD
	elif value >= (center_pos - 50) and value <= (center_pos + 50):
		return "NONE"
	else:
		dir = Adafruit_MotorHAT.BACKWARD
		print("Coarse Rotate Right")
	return dir

def rotateFine(value, center_pos, motor):
	motor.setSpeed(60)
	dir = "NONE"
	if value < (center_pos - 25):
		dir = Adafruit_MotorHAT.FORWARD
	elif value >= (center_pos - 25) and value <= (center_pos + 25):
		return "NONE"
	else:
		dir = Adafruit_MotorHAT.BACKWARD
	return dir

def tilt(value, center_pos, motor):
	motor.setSpeed(60)
	dir = "NONE"
	if value < (center_pos - 50):
		dir = Adafruit_MotorHAT.FORWARD
	elif value >= (center_pos - 50) and value <= (center_pos + 50):
		return "NONE"
	else:
		dir = Adafruit_MotorHAT.BACKWARD
	return dir

def stepper_worker(rotmotor, tiltmotor, stepnum, stepstyle):
	while True:
		event = gamepad.read_one()
		if event != None and event.type == ecodes.EV_ABS:
			event = categorize(event).event
			if event.code == 5:
				rotationCommand = rotateFine(event.value, 256, rotationMotor)
			elif event.code == 1:
				tiltCommand = tilt(event.value, 512, tiltMotor)
			elif event.code == 0:
				rotationCommand = rotateGross(event.value, 512, rotationMotor)
			else:
				rotationCommand = "NONE"
				tiltCommand = "NONE"
		if rotationCommand != "NONE":
			direction = rotationCommand
			rotationMotor.step(stepnum, direction, stepstyle)
		if tiltCommand != "NONE":
			direction = tiltCommand
			tiltMotor.step(stepnum, direction, stepstyle)

def main():
	gamepad = InputDevice('/dev/input/event0')
	atexit.register(turnOffMotors)
	rotationMotor = mh.getStepper(50, 1)
	tiltMotor = mh.getStepper(50, 2)
	app = QtWidgets.QApplication(sys.argv)
	form = RaspberryJam()
	form.show()
	app.exec_()
	rotationCommand = "NONE"
	tiltCommand = "NONE"
	st1 = threading.Thread( target=stepper_worker, args=(rotationMotor, tiltMotor, 1, Adafruit_MotorHAT.DOUBLE,) )
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()

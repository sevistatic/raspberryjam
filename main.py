#!/usr/bin/python
import sys
sys.path.append('/usr/local/lib/python3.4/site-packages')

from evdev import InputDevice, categorize, ecodes
from time import sleep
import multiprocessing as pc
import random

from PyQt5 import QtGui, QtCore, QtWidgets

import mainwindow
import armature
import jammer

FINE_X_AXIS_EVENT = 5 
GROSS_X_AXIS_EVENT = 0
Y_AXIS_EVENT = 1
programIsOpen = True

class RaspberryJam(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):

	def __init__(self, parent=None):
		super(RaspberryJam, self).__init__(parent)
		self.setupUi(self)
		self.resize(760,520)

def controlArmature(arm, jam):
	#Depending on how the devices are connected, the Saitek Joystick
	#could be any device from event0 to event4
	gamepad = InputDevice('/dev/input/event4')
	#print(gamepad)
	rotationCommand = "NONE"
	tiltCommand = "NONE"
	while programIsOpen == True:
		event = gamepad.read_one()
		if event != None:
			if event.type == ecodes.EV_ABS:
				event = categorize(event).event
				if event.code == FINE_X_AXIS_EVENT:
					if event.value < (256 - 26):
						rotationCommand = "LEFT"
					elif event.value > (256 + 26):
						rotationCommand = "RIGHT"
					else:
						rotationCommand = "NONE"
				elif event.code == Y_AXIS_EVENT:
					if event.value < (512 - 51):
						tiltCommand = "DOWN"
					elif event.value > (512 + 51):
						tiltCommand = "UP"
					else:
						tiltCommand = "NONE"
				elif event.code == GROSS_X_AXIS_EVENT:
					if event.value < (512 - 51):
						rotationCommand = "LEFT"
					elif event.value > (512 + 51):
						rotationCommand = "RIGHT"
					else:
						rotationCommand = "NONE"
			elif event.type == ecodes.EV_KEY:
				event = categorize(event)
				if event.keycode[1] is "BTN_TRIGGER":
#The following print statements are for proving the code boundaries
#for the module work without the hardware connected
					if event.keystate is 1:
						jam.start()
						#print("TRIGGER IN")
					elif event.keystate is 0:
						jam.stop()
						#print("TRIGGER OUT")
		if rotationCommand is "LEFT":
			arm.rotateLeft()
#			print("ROTATE LEFT")
		elif rotationCommand is "RIGHT":
			arm.rotateRight()
#			print("ROTATE RIGHT")
		if tiltCommand is "DOWN":
			arm.tiltDown()
#			print("TILT DOWN")
		elif tiltCommand is "UP":
			arm.tiltUp()
#			print("TILT UP")

def main():
	#This is the flag for ending the user input thread when the
	#application is closed
	global programIsOpen
	app = QtWidgets.QApplication(sys.argv)
	form = RaspberryJam()

	#initialize hardware interface modules
	arm = armature.Armature()
	jam = jammer.Jammer()

	#begin user input thread
	process = pc.Process( target=controlArmature, args=(arm,jam))
	process.start()

	#center and fix the size of the application window
	form.show()
	form.setFixedSize(760,520)
	screen = app.desktop()
	geometry = screen.availableGeometry()
	screenWidth = geometry.width()
	screenHeight = geometry.height()
	x = screenWidth / 2 - (760 / 2)
	y = screenHeight / 2 - (520 / 2)
	form.move(x,y)
	
	app.exec_()
	#Set flag after program closes
	programIsOpen = False

if __name__ == '__main__':
	main()

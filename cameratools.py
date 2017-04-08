import numpy as np
import cv2
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
#self.layout = QtWidgets.QHBoxLayout(self.cameraFrame)
class CameraWidget(QtWidgets.QLabel):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		print("camera widget initialized")
		self.cap = cv2.VideoCapture(0)

	def __del__(self):
		print("camera widget destroyed")
		self.cap.release()
		cv2.destroyAllWindows()

	def paintEvent(self, QPaintEvent):
		super(CameraWidget, self).paintEvent(QPaintEvent)
		print("paint even called")
		painter = QtGui.QPainter()
		ret, frame = self.cap.read()
		painter.begin(self)
		if(self.cap.isOpened()):
			print("cap is opened")
			if ret:
				print("ret is a useful value")
				ret, frame = self.cap.read()
				rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				bytesPerFrame = 3 * rgb_frame.shape[1]
				mQImage = QtGui.QImage(rgb_frame.tobytes(), rgb_frame.shape[1], rgb_frame.shape[0], QtGui.QImage.Format_RGB888)
				if mQImage:
					pixmap = QtGui.QPixmap.fromImage(mQImage)
					#painter.drawImage(10, 10, mQImage)
					#pixmap.save("/home/pi/Desktop/wierd.jpg")
					#painter.drawLine(10,10, 100, 100)
					self.setPixmap(pixmap)
				else:
					print("no mqImage")
#				cv2.imshow("cam", frame)
			else:
				print("cap returned something bad")
		else:
			print("cap is not open")
		painter.end()

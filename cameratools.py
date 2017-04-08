import numpy as np
import cv2
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
#self.layout = QtWidgets.QHBoxLayout(self.cameraFrame)
class CameraWidget(QtWidgets.QLabel):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.cap = cv2.VideoCapture(0)

	def __del__(self):
		self.cap.release()
		cv2.destroyAllWindows()

	def paintEvent(self, QPaintEvent):
		super(CameraWidget, self).paintEvent(QPaintEvent)
		painter = QtGui.QPainter()
		ret, frame = self.cap.read()
		painter.begin(self)
		if(self.cap.isOpened()):
			if ret:
				ret, frame = self.cap.read()
				rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				bytesPerFrame = 3 * rgb_frame.shape[1]
				mQImage = QtGui.QImage(rgb_frame.tobytes(), rgb_frame.shape[1], rgb_frame.shape[0], QtGui.QImage.Format_RGB888)
				if mQImage:
					pixmap = QtGui.QPixmap.fromImage(mQImage)
					self.setPixmap(pixmap)
		painter.end()

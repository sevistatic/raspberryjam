import numpy as np
import cv2
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

class CameraWidget(QtWidgets.QLabel):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		#load the videocapture device
		self.cap = cv2.VideoCapture(0)

	#release the capture device when the application closes
	def __del__(self):
		self.cap.release()

	#paints the camera frame into widget when the UI is painted
	def paintEvent(self, QPaintEvent):
		super(CameraWidget, self).paintEvent(QPaintEvent)
		painter = QtGui.QPainter()

		#begin painting the widget	
		painter.begin(self)
		if(self.cap.isOpened()):
			#ret = False if there is nothing to capture
			#frame is the image data in BGR mode
			ret, frame = self.cap.read()
			if ret:
				#switch blue and red positions
				#opencv uses blue first
				#pyqt uses red first
				rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				height = rgb_frame.shape[0]
				width = rgb_frame.shape[1]
				bytesPerFrame = 3 * rgb_frame.shape[1]
				mQImage = QtGui.QImage(rgb_frame.tobytes(), width, height, QtGui.QImage.Format_RGB888)
				if mQImage:
					pixmap = QtGui.QPixmap.fromImage(mQImage)
					self.setPixmap(pixmap)
		#close the painter, so it knows to finish drawing the frame
		painter.end()

import numpy as np
import cv2
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

rekt = QtCore.QRectF(0,0,0,0)

class CameraWidget(QtWidgets.QLabel):

	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		#load the videocapture device
		self.cap = cv2.VideoCapture(0)

	#release the capture device when the application closes
	def __del__(self):
		self.cap.release()

	#shrinks and enlarges the rectangle to be painted in the paintEvent step
	def toggleOverlay(self):
		global rekt
		if rekt.width() < 1:
			rekt = QtCore.QRectF(160,120,320,240)
		else:
			rekt = QtCore.QRectF(0,0,0,0)

	#paints the camera frame into widget when the UI is painted
	def paintEvent(self, QPaintEvent):
		super(CameraWidget, self).paintEvent(QPaintEvent)
		painter = QtGui.QPainter()
		global rekt
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

					#paint a crosshair in the center
					pen = QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin);
					painter.setPen(pen)
					painter.drawLine(300, 240, 340, 240)
					painter.drawLine(320, 220, 320, 260)

					painter.setBrush(QtGui.QColor(255, 0, 0, 127))
					painter.drawEllipse(rekt)
		#close the painter, so it knows to finish drawing the frame
		painter.end()

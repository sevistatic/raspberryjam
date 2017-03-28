from PyQt5 import QtGui, QtCore, QtWidgets
import sys

import mainwindow

class RaspberryJam(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):

	def __init__(self, parent=None):
		super(RaspberryJam, self).__init__(parent)
		self.setupUi(self)
def main():
	app = QtWidgets.QApplication(sys.argv)
	form = RaspberryJam()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()

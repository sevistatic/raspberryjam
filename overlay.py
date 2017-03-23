import sys
from PyQt4 import QtGui

def window():
	app = QtGui.QApplication(sys.argv)
	w = QtGui.QWidget()
	b = QtGui.QLabel(w)
	b.setText("Hey, y'all")
	w.setGeometry(150,150,650,50)
	b.move(50,20)
	w.setWindowTitle("PtQt")
	w.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	window()

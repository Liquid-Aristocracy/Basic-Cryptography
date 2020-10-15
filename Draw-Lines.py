import sys
from PyQt5 import QtCore, QtWidgets, QtGui


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # variables
        self.Top = 20
        self.Left = 0
        self.Width = 1200
        self.Height = 820
        self.Ox = 600
        self.Oy = 400 + self.Top
        # set properties of window
        self.setWindowTitle("Drawing")
        self.setGeometry(400, 150, self.Width, self.Height)
        # set menu
        self.menuDrawLine = self.menuBar().addMenu("Line")
        self.menuDrawLine.addAction("DDA...")
        # show
        self.show

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter()
        painter.begin(self)
        # draw mesh
        painter.setPen(QtGui.QPen(QtGui.QColor("#999999"), 2, QtCore.Qt.SolidLine))
        for i in range(8):
            painter.drawLine(self.Left, i*100 + self.Top, self.Width, i*100 + self.Top)
        for i in range(12):
            painter.drawLine(i*100, self.Top, i*100, self.Height)
        # draw axis
        painter.setPen(QtGui.QPen(QtGui.QColor("#000000"), 2, QtCore.Qt.SolidLine))
        painter.drawLine(self.Left, self.Oy, self.Width, self.Oy)
        painter.drawLine(self.Ox, self.Top, self.Ox, self.Height)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Window()
    gui.show()
    sys.exit(app.exec_())

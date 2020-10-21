import sys
from PyQt5 import QtCore, QtWidgets, QtGui


def emptyFunc(self, *args):
    pass


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
        self.drawArgs = ()
        self.drawFunc = emptyFunc
        self.menuDrawLine = self.menuBar().addMenu("Line")
        self.menuDrawLine.addAction("DDA...")
        self.menuDrawLine.addAction("Bresenham...")
        # show
        self.show
        print(self.drawFunc)

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
        # draw graph
        self.drawFunc(self, *self.drawArgs)

    def myPaint(self, function, *args):
        self.drawFunc = function()
        self.drawArgs = args
        self.update()

    def lineDDA(self, x1, y1, x2, y2):
        # set painter
        linepainter = QtGui.QPainter()
        linepainter.begin(self)
        linepainter.setPen(QtGui.QPen(QtGui.QColor("#990000"), 2, QtCore.Qt.SolidLine))
        # choose start point
        if y2 < y1:
            t = x1
            x1 = x2
            x2 = t
            t = y1
            y1 = y2
            y2 = t
        # DDA
        xk = x1
        yk = y1
        if abs(x1 - x2) > abs(y1 - y2):
            steps = abs(x1 - x2)
        else:
            steps = abs(y1 - y2)
        dx = (x1 - x2) / steps
        dy = (y1 - y2) / steps
        for i in range(steps):
            linepainter.drawPoint(self, round(xk), round(yk))
            xk += dx
            yk += dy

    def lineBresenham(self, x1, y1, x2, y2):
        # set painter
        linepainter = QtGui.QPainter()
        linepainter.begin(self)
        linepainter.setPen(QtGui.QPen(QtGui.QColor("#990000"), 2, QtCore.Qt.SolidLine))
        # choose start point
        if y2 < y1:
            t = x1
            x1 = x2
            x2 = t
            t = y1
            y1 = y2
            y2 = t
        # Bresenham
        xk = x1
        yk = y1
        if abs(x1 - x2) > abs(y1 - y2):
            p = 2 * (y1 - y2) - (x1 - x2)
            delta1 = 2 * (y1 - y2)
            delta2 = 2 * (y1 - y2) - 2 * (x1 - x2)
            if x2 > x1:
                dx = 1
            else:
                dx = -1
            while xk <= x2:
                linepainter.drawPoint(self, xk, yk)
                xk += dx
                if p < 0:
                    p += delta1
                else:
                    yk += 1
                    p += delta2
        else:
            p = 2 * (x1 - x2) - (y1 - y2)
            delta1 = 2 * (x1 - x2)
            delta2 = 2 * (x1 - x2) - 2 * (y1 - y2)
            if y2 > y1:
                dy = 1
            else:
                dy = -1
            while yk <= y2:
                linepainter.drawPoint(self, xk, yk)
                yk += dy
                if p < 0:
                    p += delta1
                else:
                    yk += 1
                    p += delta2


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Window()
    gui.show()
    sys.exit(app.exec_())

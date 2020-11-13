import sys
import time
from PyQt5 import QtCore, QtWidgets, QtGui


class Window(QtWidgets.QMainWindow):
    class Dialog(QtWidgets.QWidget):
        def __init__(self, main, fun):
            super().__init__(main)
            self.mainWindow = main
            self.setGeometry(main.Width - 500, main.Top, 500, main.Height)
            self.setStyleSheet("border-style: solid; border-width: 2px; border-color: #999999; background-color: #484848; color: #FFFFFF")
            self.show()
            self.setWindowTitle(fun)
            self.numOnly = QtGui.QDoubleValidator()
            # choose which to draw
            self.choose = QtWidgets.QComboBox(self)
            self.choose.setFont(QtGui.QFont("Consolas", 20))
            self.choose.resize(400, 50)
            self.choose.move(50, 50)
            self.choose.addItems(["DDA", "Bresenham", "MidCircle", "MidEclipse"])
            self.choose.activated.connect(self.restart)
            self.choose.setStyleSheet("QComboBox{border: 0px} QComboBox::drop-down{width: 400 px; border: 0px solid}")
            self.choose.show()
            # arg1
            self.label1 = QtWidgets.QLabel(self)
            self.label1.setText("X0")
            self.label1.setStyleSheet("border-width: 0px")
            self.label1.resize(50, 50)
            self.label1.move(50, 150)
            self.label1.setFont(QtGui.QFont("Consolas", 18))
            self.label1.show()
            self.input1 = QtWidgets.QLineEdit('', self)
            self.input1.setValidator(self.numOnly)
            self.input1.resize(300, 50)
            self.input1.move(100, 150)
            self.input1.setFont(QtGui.QFont("Consolas", 18))
            self.input1.show()
            # arg2
            self.label2 = QtWidgets.QLabel(self)
            self.label2.setText("Y0")
            self.label2.setStyleSheet("border-width: 0px")
            self.label2.resize(50, 50)
            self.label2.move(50, 250)
            self.label2.setFont(QtGui.QFont("Consolas", 18))
            self.label2.show()
            self.input2 = QtWidgets.QLineEdit('', self)
            self.input2.setValidator(self.numOnly)
            self.input2.resize(300, 50)
            self.input2.move(100, 250)
            self.input2.setFont(QtGui.QFont("Consolas", 18))
            self.input2.show()
            # arg3
            self.label3 = QtWidgets.QLabel(self)
            self.label3.setText("X1")
            self.label3.setStyleSheet("border-width: 0px")
            self.label3.resize(50, 50)
            self.label3.move(50, 350)
            self.label3.setFont(QtGui.QFont("Consolas", 18))
            self.label3.show()
            self.input3 = QtWidgets.QLineEdit('', self)
            self.input3.setValidator(self.numOnly)
            self.input3.resize(300, 50)
            self.input3.move(100, 350)
            self.input3.setFont(QtGui.QFont("Consolas", 18))
            self.input3.show()
            # arg4
            self.label4 = QtWidgets.QLabel(self)
            self.label4.setText("Y1")
            self.label4.setStyleSheet("border-width: 0px")
            self.label4.resize(50, 50)
            self.label4.move(50, 450)
            self.label4.setFont(QtGui.QFont("Consolas", 18))
            self.label4.show()
            self.input4 = QtWidgets.QLineEdit('', self)
            self.input4.setValidator(self.numOnly)
            self.input4.resize(300, 50)
            self.input4.move(100, 450)
            self.input4.setFont(QtGui.QFont("Consolas", 18))
            self.input4.show()
            # if instant draw
            self.instant = QtWidgets.QCheckBox(self)
            self.instant.setText("Instant")
            self.instant.setStyleSheet("QCheckBox{border: 0px}\
                                        QCheckBox::indicator::unchecked{background: #999999} QCheckBox::indicator::unchecked:hover{background: #ffffff} QCheckBox::indicator::unchecked:pressed{background: #999999}\
                                        QCheckBox::indicator::checked{background: #007acc}  QCheckBox::indicator::checked:hover{background: #00adef} QCheckBox::indicator::checked:pressed{background: #007acc}")
            self.instant.setFont(QtGui.QFont("Consolas", 12))
            self.instant.resize(200, 50)
            self.instant.move(305, 550)
            self.instant.show()
            # start draw
            self.ok = QtWidgets.QPushButton(self)
            self.ok.setText("Draw")
            self.ok.setFont(QtGui.QFont("Consolas", 20))
            self.ok.setStyleSheet("QPushButton:hover{border: 0px solid; background-color: #007acc}\
                                   QPushButton:pressed{border: 2px solid; background-color: #484848; border-color: #999999}")
            self.ok.resize(100, 50)
            self.ok.move(300, 600)
            self.ok.show()
            self.ok.clicked.connect(self.drawpushed)
            # clear all
            self.cl = QtWidgets.QPushButton(self)
            self.cl.setText("Clear")
            self.cl.setFont(QtGui.QFont("Consolas", 20))
            self.cl.setStyleSheet("QPushButton{border: 0px solid; color: #999999} QPushButton:hover{border: 0px solid; background-color: #999999; color: #484848}\
                                   QPushButton:pressed{border: 2px solid; background-color: #484848; border-color: #999999; color: #999999}")
            self.cl.resize(100, 50)
            self.cl.move(150, 600)
            self.cl.show()
            self.cl.clicked.connect(self.mainWindow.canvas.clear)

        def drawpushed(self):
            text = self.choose.currentText()
            t = []
            t.append(self.input1.text())
            t.append(self.input2.text())
            t.append(self.input3.text())
            t.append(self.input4.text())
            for input in range(4):
                if t[input] == '':
                    t[input] = "0"
            self.mainWindow.canvas.getfun(text, float(t[0]), float(t[1]), float(t[2]), float(t[3]))

        def restart(self):
            # clear all args
            text = self.choose.currentText()
            if text == "DDA" or text == "Bresenham":
                self.input4.show()
                self.label4.show()
                self.input1.clear()
                self.input2.clear()
                self.input3.clear()
                self.input4.clear()
                self.label1.setText("X0")
                self.label2.setText("Y0")
                self.label3.setText("X1")
                self.label4.setText("Y1")
            elif text == "MidCircle":
                self.input4.hide()
                self.label4.hide()
                self.input1.clear()
                self.input2.clear()
                self.input3.clear()
                self.input4.setText("0")
                self.label1.setText("X")
                self.label2.setText("Y")
                self.label3.setText("R")
            elif text == "MidEclipse":
                self.input4.show()
                self.label4.show()
                self.input1.clear()
                self.input2.clear()
                self.input3.clear()
                self.input4.clear()
                self.label1.setText("X")
                self.label2.setText("Y")
                self.label3.setText("A")
                self.label4.setText("B")

    class Canvas(QtWidgets.QWidget):

        def __init__(self, main):
            super().__init__(main)
            self.mainWindow = main
            self.resize(self.mainWindow.Width - 500, self.mainWindow.Height)
            self.func = 0
            self.points = []

        def clear(self):
            self.points = []
            self.repaint()

        def getfun(self, fun, in1=0, in2=0, in3=20, in4=20):
            self.func = fun
            self.in1 = in1
            self.in2 = in2
            self.in3 = in3
            self.in4 = in4
            self.repaint()
            waittime = 0.01
            if self.func == "DDA":
                x1 = self.in1
                y1 = self.in2
                x2 = self.in3
                y2 = self.in4
                if x1 == x2 and y1 == y2:
                    return
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
                dx = (x2 - x1) / steps
                dy = (y2 - y1) / steps
                for i in range(steps):
                    self.points.append((600 + round(xk), 400 - round(yk)))
                    if self.mainWindow.dialog.instant.isChecked() == 0:
                        self.repaint()
                        time.sleep(waittime)
                    else:
                        self.update()
                    xk += dx
                    yk += dy
            elif self.func == "Bresenham":
                x1 = self.in1
                y1 = self.in2
                x2 = self.in3
                y2 = self.in4
                if x1 == x2 and y1 == y2:
                    return
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
                    p = 2 * (y2 - y1) - (x2 - x1)
                    delta1 = 2 * (y2 - y1)
                    delta2 = 2 * (y2 - y1) - 2 * (x2 - x1)
                    if x2 > x1:
                        dx = 1
                    else:
                        dx = -1
                    while xk <= x2:
                        self.points.append((600 + xk, 400 - yk))
                        if self.mainWindow.dialog.instant.isChecked() is False:
                            self.repaint()
                            time.sleep(0.01)
                        else:
                            self.update()
                        xk += dx
                        if p < 0:
                            p += delta1
                        else:
                            yk += 1
                            p += delta2
                else:
                    p = 2 * (x2 - x1) - (y2 - y1)
                    delta1 = 2 * (x2 - x1)
                    delta2 = 2 * (x2 - x1) - 2 * (y2 - y1)
                    if y2 > y1:
                        dy = 1
                    else:
                        dy = -1
                    while yk <= y2:
                        self.points.append((600 + xk, 400 - yk))
                        if self.mainWindow.dialog.instant.isChecked() is False:
                            self.repaint()
                            time.sleep(waittime)
                        else:
                            self.update()
                        yk += dy
                        if p < 0:
                            p += delta1
                        else:
                            xk += 1
                            p += delta2
            elif self.func == "MidCircle":
                x = self.in1
                y = self.in2
                r = self.in3
                if r == 0:
                    return
                p = 5 / 4 - r
                xk = 0
                yk = r
                while xk <= yk:
                    self.points.append((600 + xk + x, 400 - yk - y))
                    self.points.append((600 + xk + x, 400 + yk - y))
                    self.points.append((600 - xk + x, 400 - yk - y))
                    self.points.append((600 - xk + x, 400 + yk - y))
                    self.points.append((600 + yk + x, 400 - xk - y))
                    self.points.append((600 + yk + x, 400 + xk - y))
                    self.points.append((600 - yk + x, 400 - xk - y))
                    self.points.append((600 - yk + x, 400 + xk - y))
                    if self.mainWindow.dialog.instant.isChecked() is False:
                        self.repaint()
                        time.sleep(waittime)
                    else:
                        self.update()
                    xk += 1
                    if p < 0:
                        p = p + 2 * xk + 1
                    else:
                        yk -= 1
                        p = p + 2 * xk + 1 - 2 * yk
            elif self.func == "MidEclipse":
                x = self.in1
                y = self.in2
                a = self.in3
                b = self.in4
                xk = 0
                yk = b
                if a == 0 and b == 0:
                    return
                p = b ** 2 - (a ** 2) * b + 0.25 * (a ** 2)
                px = 2 * (b ** 2) * xk
                py = 2 * (a ** 2) * yk
                dpx = (b ** 2)
                dpy = (a ** 2)
                while px < py:
                    self.points.append((600 + xk + x, 400 - yk - y))
                    self.points.append((600 + xk + x, 400 + yk - y))
                    self.points.append((600 - xk + x, 400 - yk - y))
                    self.points.append((600 - xk + x, 400 + yk - y))
                    if self.mainWindow.dialog.instant.isChecked() is False:
                        self.repaint()
                        time.sleep(waittime)
                    else:
                        self.update()
                    xk += 1
                    px += 2 * dpx
                    if p < 0:
                        p = p + px + dpx
                    else:
                        yk -= 1
                        py -= 2 * dpy
                        p = p + px - py + dpx
                p = dpx * ((xk + 0.5) ** 2) + dpy * ((yk - 1) ** 2) - dpx * dpy
                while yk != 0:
                    self.points.append((600 + xk + x, 400 - yk - y))
                    self.points.append((600 + xk + x, 400 + yk - y))
                    self.points.append((600 - xk + x, 400 - yk - y))
                    self.points.append((600 - xk + x, 400 + yk - y))
                    if self.mainWindow.dialog.instant.isChecked() is False:
                        self.repaint()
                        time.sleep(waittime)
                    else:
                        self.update()
                    yk -= 1
                    py -= 2 * dpy
                    if p > 0:
                        p = p - py + dpy
                    else:
                        xk += 1
                        px += 2 * dpx
                        p = p + px - py + dpy

        def paintEvent(self, QPaintEvent):
            linepainter = QtGui.QPainter()
            linepainter.begin(self)
            linepainter.setPen(QtGui.QPen(QtGui.QColor("#00adef"), 2, QtCore.Qt.SolidLine))
            for i in self.points:
                linepainter.drawPoint(i[0], i[1])

    def __init__(self):
        super().__init__()
        # variables
        self.Top = 0
        self.Left = 0
        self.Width = 1700
        self.Height = 800
        self.Ox = 600
        self.Oy = 400 + self.Top
        # set properties of window
        self.setWindowTitle("Drawing")
        self.setGeometry(100, 100, self.Width, self.Height)
        self.setStyleSheet("border-style: solid; border-width: 0px; background-color: #484848")
        self.show()
        # set menu
        self.xlabel = QtWidgets.QLabel(self)
        self.xlabel.setText("100")
        self.xlabel.setFont(QtGui.QFont("Consolas", 12))
        self.xlabel.setStyleSheet("border-width: 0px; color: #999999")
        self.xlabel.resize(30, 20)
        self.xlabel.move(702, 401)
        self.xlabel.show()
        self.ylabel = QtWidgets.QLabel(self)
        self.ylabel.setText("100")
        self.ylabel.setFont(QtGui.QFont("Consolas", 12))
        self.ylabel.setStyleSheet("border-width: 0px; color: #999999")
        self.ylabel.resize(30, 20)
        self.ylabel.move(568, 279)
        self.ylabel.show()
        self.olabel = QtWidgets.QLabel(self)
        self.olabel.setText("O")
        self.olabel.setFont(QtGui.QFont("Consolas", 12))
        self.olabel.setStyleSheet("border-width: 0px; color: #999999")
        self.olabel.resize(15, 20)
        self.olabel.move(583, 401)
        self.olabel.show()
        self.canvas = self.Canvas(self)
        self.dialog = self.Dialog(self, "")
        self.canvas.show()

    def startDraw(self, funname):
        self.ask = self.Dialog(self, funname)
        self.ask.show()

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter()
        painter.begin(self)
        # draw mesh
        painter.setPen(QtGui.QPen(QtGui.QColor("#999999"), 2, QtCore.Qt.SolidLine))
        for i in range(9):
            painter.drawLine(self.Left, i*100 + self.Top, self.Width - 500, i*100 + self.Top)
        for i in range(13):
            painter.drawLine(i*100, self.Top, i*100, self.Height)
        # draw axis
        painter.setPen(QtGui.QPen(QtGui.QColor("#FFFFFF"), 2, QtCore.Qt.SolidLine))
        painter.drawLine(self.Left, self.Oy, self.Width - 500, self.Oy)
        painter.drawLine(self.Ox, self.Top, self.Ox, self.Height)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    gui = Window()
    gui.show()
    sys.exit(app.exec_())

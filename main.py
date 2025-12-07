import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np


form_class = uic.loadUiType("main.ui")[0]


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.f = {}
        self.g = {}

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        self.graph_verticalLayout.addWidget(self.canvas)

        self.f_input.clicked.connect(self.finput)
        self.g_input.clicked.connect(self.ginput)
        self.graph_button.clicked.connect(self.run)

    def finput(self):
        index = int(self.f_index.toPlainText())
        number = self.f_number.toPlainText()
        if '.' in number:
            number = float(number)
        else:
            number = int(number)
        if index in list(self.f.keys()):
            self.f[index] += number
        else:
            self.f[index] = number
        self.f_index.clear()
        self.f_number.clear()

        self.f = dict(sorted(self.f.items(), reverse=True))

        f = ''
        for index in list(self.f.keys()):
            number = self.f[index]
            if index != 0:
                f += f"{number}x^^{index} + "
            else:
                f += f"{number}"
        self.fx.setText(f)

    def ginput(self):
        index = int(self.g_index.toPlainText())
        number = self.g_number.toPlainText()
        if '.' in number:
            number = float(number)
        else:
            number = int(number)
        if index in list(self.g.keys()):
            self.g[index] += number
        else:
            self.g[index] = number
        self.g_index.clear()
        self.g_number.clear()

        self.g = dict(sorted(self.g.items(), reverse=True))

        g = ''
        for index in list(self.g.keys()):
            number = self.g[index]
            if index != 0:
                g += f"{number}x^^{index} + "
            else:
                g += f"{number}"
        self.gx.setText(g)

    def run(self):
        x = np.arange(-100,100,1)
        y = np.array([self.fg_function(x_x) for x_x in x.tolist()])

        ax = self.fig.add_subplot(111)
        ax.plot(x, y, label='f(g(x))')
        ax.set_xlabel("x")
        ax.set_xlabel("y")

        y = np.array([self.f_function(x_x) for x_x in x.tolist()])

        ax.plot(x, y, label='f(x)')

        y = np.array([self.g_function(x_x) for x_x in x.tolist()])

        ax.plot(x, y, label='g(x)')

        ax.set_title("graph")
        ax.legend()
        self.canvas.draw()



    def fg_function(self, x):
        x = int(x)
        g = 0
        f = 0
        for index in list(self.g.keys()):
            g += self.g[index] * (x**index)
        for index in list(self.f.keys()):
            f += self.f[index] * (g**index)
        return f

    def f_function(self, x):
        x = int(x)
        f = 0
        for index in list(self.f.keys()):
            f += self.f[index] * (x**index)
        return f

    def g_function(self, x):
        x = int(x)
        g = 0
        for index in list(self.g.keys()):
            g += self.g[index] * (x**index)
        return g


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()

    app.exec_()
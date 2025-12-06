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

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        self.graph_verticalLayout.addWidget(self.canvas)

        self.graph_button.clicked.connect(self.run)

    def run(self):
        x = np.arange(-100,100,1)
        y = np.array([self.function(x_x) for x_x in x.tolist()])

        ax = self.fig.add_subplot(111)
        ax.plot(x,y)
        ax.set_xlabel("x")
        ax.set_xlabel("y")

        ax.set_title("graph")
        self.canvas.draw()



    def function(self, x):
        x = int(x)
        g = float(self.g_double.toPlainText())*(x**2) + float(self.g_x.toPlainText())*x + float(self.g_number.toPlainText())
        f = float(self.f_double.toPlainText())*(g**2) + float(self.f_x.toPlainText())*g + float(self.g_number.toPlainText())
        return f

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()

    app.exec_()
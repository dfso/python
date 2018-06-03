# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 17:48:50 2018

@author: dfso
"""
import sys
from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.titulo = "PyQt5 Window @dfso"
        self.top = 200
        self.left = 200
        self.largura = 640
        self.altura = 480

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.titulo)
        self.setGeometry(self.top, self.left,
                         self.largura, self.altura)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'threads_testing.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(QtWidgets.QWidget):
    def setup_ui(self, window):

        self.setGeometry(200, 200, 720, 480)
        self.setWindowTitle("Threads Testing")

        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.progressBar_1 = QtWidgets.QProgressBar()
        self.progressBar_1.setProperty("value", 0)
        self.verticalLayout.addWidget(self.progressBar_1)

        self.progressBar_2 = QtWidgets.QProgressBar()
        self.progressBar_2.setProperty("value", 0)
        self.verticalLayout.addWidget(self.progressBar_2)

        self.progressBar_3 = QtWidgets.QProgressBar()
        self.progressBar_3.setProperty("value", 0)
        self.verticalLayout.addWidget(self.progressBar_3)

        self.btn_start = QtWidgets.QPushButton("start threads")
        self.verticalLayout.addWidget(self.btn_start)

        self.btn_stop = QtWidgets.QPushButton("stop threads")
        self.verticalLayout.addWidget(self.btn_stop)

        self.setLayout(self.verticalLayout)

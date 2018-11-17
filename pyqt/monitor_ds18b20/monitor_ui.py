# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MonitorUI(QtWidgets.QWidget):
    def setup_ui(self, window):
        self.setGeometry(200, 200, 640, 290)
        self.setWindowTitle("Monitor DS18B20 @dfso")

        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel("Temperatura")

        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.label_temp = QtWidgets.QLabel("°C")
        self.label_temp.setMaximumWidth(self.width())

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        font.setWeight(50)

        self.label_temp.setFont(font)
        self.label_temp.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.label_temp)
        self.setLayout(self.verticalLayout)

        
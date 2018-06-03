# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lista = QtWidgets.QListWidget(self.centralwidget)
        self.lista.setObjectName("lista")
        self.horizontalLayout.addWidget(self.lista)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName("menubar")
        self.menu_acoes = QtWidgets.QMenu(self.menubar)
        self.menu_acoes.setObjectName("menu_acoes")
        self.menu_sobre = QtWidgets.QMenu(self.menubar)
        self.menu_sobre.setObjectName("menu_sobre")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_verificar = QtWidgets.QAction(MainWindow)
        self.action_verificar.setObjectName("action_verificar")
        self.menu_acoes.addAction(self.action_verificar)
        self.menubar.addAction(self.menu_acoes.menuAction())
        self.menubar.addAction(self.menu_sobre.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Atualizador @dfso"))
        self.menu_acoes.setTitle(_translate("MainWindow", "&Ações"))
        self.menu_sobre.setTitle(_translate("MainWindow", "Sobre..."))
        self.action_verificar.setText(_translate("MainWindow", "&Verificar atualizações"))
        self.action_verificar.setShortcut(_translate("MainWindow", "F5"))


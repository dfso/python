# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
import threading

class Ui_MainWindow():

    arduino = QtSerialPort.QSerialPort()

    temp = ''
    def getPortas(self):
        portas = QtSerialPort.QSerialPortInfo.availablePorts()
        print("Portas encontradas:")
        print('------------------')
        for p in portas:
            print(p.portName())
        #self.comboBoxPortas.addItem("/dev/ttyUSB0")

        print('------------------')

    def lerPorta(self):
        self.arduino.setPortName("/dev/ttyUSB0")
        self.arduino.setBaudRate(9600)
        self.arduino.open(QtCore.QIODevice.ReadOnly)

        print("Conectado" if self.arduino.isOpen() else "Falhou ao conectar")
        data = QtCore.QByteArray()
        while self.arduino.waitForReadyRead(1):
            data.append(self.arduino.readAll())
        self.temp = bytearray(data)
        print("obtendo dados...")
        print (self.temp.decode("utf8"))
        print(self.temp.__len__())
        self.arduino.close()

    def sair(self):
        self.arduino.close()
        if not self.arduino.isOpen():
            print("fechou a conexão")
        QtWidgets.QMainWindow.close()


    def limpar(self):
        self.textEditData.setText("")

    def __init__(self):
        self.getPortas()
        self.lerPorta()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(548, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelPortas = QtWidgets.QLabel(self.centralwidget)
        self.labelPortas.setObjectName("labelPortas")
        self.horizontalLayout.addWidget(self.labelPortas)
        self.comboBoxPortas = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxPortas.setObjectName("comboBoxPortas")
        self.comboBoxPortas.addItem("/dev/ttyUSB0")

        self.horizontalLayout.addWidget(self.comboBoxPortas)
        self.btnConectar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConectar.setObjectName("btnConectar")
        self.horizontalLayout.addWidget(self.btnConectar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelBauds = QtWidgets.QLabel(self.centralwidget)
        self.labelBauds.setObjectName("labelBauds")
        self.horizontalLayout_2.addWidget(self.labelBauds)
        self.comboBoxBauds = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxBauds.setObjectName("comboBoxBauds")
        self.comboBoxBauds.addItem("")
        self.comboBoxBauds.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBoxBauds)
        self.btnSair = QtWidgets.QPushButton(self.centralwidget)
        self.btnSair.setObjectName("btnSair")
        self.horizontalLayout_2.addWidget(self.btnSair)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEditData = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditData.setObjectName("textEditData")
        self.textEditData.setText(self.temp.decode("utf-8"))
        self.verticalLayout_2.addWidget(self.textEditData)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        #self.btnSair.clicked.connect(self.sair)
        self.btnSair.clicked.connect(MainWindow.close)
        self.btnConectar.clicked.connect(self.limpar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SerialComm @dfso"))
        self.labelPortas.setText(_translate("MainWindow", "Selecione a porta"))
        self.btnConectar.setText(_translate("MainWindow", "Conectar"))
        self.labelBauds.setText(_translate("MainWindow", "Baud rate"))
        self.comboBoxBauds.setItemText(0, _translate("MainWindow", "9600"))
        self.comboBoxBauds.setItemText(1, _translate("MainWindow", "115200"))
        self.btnSair.setText(_translate("MainWindow", "Sair"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

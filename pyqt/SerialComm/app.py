# -*- coding: utf-8 -*-
# encoding=utf8

import sys
import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal

import serial.tools.list_ports

import SerialComm


class App(QtWidgets.QWidget, SerialComm.Ui_Form):

    arduino = None

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        print(QtWidgets.QStyleFactory.keys())
        self.setupUi(self)

        self.btn_conectar.clicked.connect(self.abrir_porta)
        self.btn_desconectar.clicked.connect(self.fechar_porta)
        self.btn_atualizar.clicked.connect(self.obter_portas)
        self.btn_desconectar.setDisabled(True)
        self.text_log.setReadOnly(True)

        if self.comboBox_portas.count() == 0:
            self.btn_conectar.setDisabled(True)
        
        self.read_thread = ReadThread()

    def obter_portas(self):
        """[obtem as portas 'comm' disponíveis no sistema]
        Returns:
        [portas] -- [uma lista das portas comm disponíveis]
        """
        self.comboBox_portas.clear()

        portas = serial.tools.list_ports.comports()

        for p in portas:
            self.comboBox_portas.addItem(p.device)
            print(p.device)

        if self.comboBox_portas.count() > 0:
            self.btn_conectar.setEnabled(True)

        return portas

    def abrir_porta(self):
        a = ReadThread().conecta(self.comboBox_portas.currentText(),
        self.comboBox_bauds.currentText())

        self.arduino = serial.Serial(self.comboBox_portas.currentText(),
                                     self.comboBox_bauds.currentText())

        self.arduino.flush()
        if self.arduino.is_open:
            self.btn_desconectar.setEnabled(True)
            self.btn_conectar.setDisabled(True)

        self.append_text(
            "Conectado: {}".format(self.arduino.is_open))

        self.read_thread.start()
        self.read_thread.dados_recebidos.connect(self.append_text)

        self.obter_dados()

    def fechar_porta(self):
        if self.arduino.is_open:
            self.arduino.close()
            self.btn_conectar.setEnabled(True)
            self.btn_desconectar.setDisabled(True)
            self.append_text(
                "Desconectado: {}".format(not self.arduino.is_open))
        self.read_thread.stop()
        self.append_text("thread is running? {}".format(self.read_thread.running))

    def obter_dados(self):
        data = self.arduino.readline().decode()
        print(data)
        self.append_text(data)

        return data

    def append_text(self, txt):
        self.text_log.appendPlainText(txt)


class ReadThread(QtCore.QThread):

    arduino = App.arduino

    dados_recebidos = pyqtSignal(str)

    def __init__(self, parent=None):
        super(ReadThread, self).__init__(parent)

        self.running = False
    
    @staticmethod
    def conecta(self, device, baud):
        arduino = serial.Serial(device, baud)
        return arduino
    
    def stop(self):
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            data = "enviando"
            self.dados_recebidos.emit(data)
            #print(self.arduino.is_open)
            time.sleep(2)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

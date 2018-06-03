import sys
import os
import time
import subprocess

from PyQt5 import QtWidgets, QtCore, QtGui

import atualizador_GUI


class App(QtWidgets.QMainWindow, atualizador_GUI.Ui_MainWindow):

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)

        #self.lista.setCurrentRow(3)
        self.lista.currentItemChanged.connect(self.info)


        self.action_verificar.triggered.connect(self.verificar_updates)


    def verificar_updates(self):
        saida = subprocess.run(
            ['ls'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        
        linhas = saida.split("\n")

        nomes = ['dfso', 'claudinha', 'mimi', 'dudu']
        self.lista.addItems(nomes)

        self.lista.addItems(linhas)


    def info(self):
        self.statusbar.showMessage("Selecionado: {}".format(
            self.lista.currentRow()))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

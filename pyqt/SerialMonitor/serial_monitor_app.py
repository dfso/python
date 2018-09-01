# -*- coding: utf-8 -*-

import sys
import functools
import serial.tools.list_ports
from PyQt5 import QtWidgets, QtGui

import gui
from serial_thread import SerialThread


class App(QtWidgets.QMainWindow, gui.Ui_MainWindow):

    arduino = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.setStyleSheet(open("style.qss", "r").read())
        # self.style_app(3)
        self.text_log.setReadOnly(True)
        self.actionDesconectar.setDisabled(True)

        self.reload_ports()

        self.actionAtualizar.triggered.connect(self.reload_ports)
        self.actionConectar.triggered.connect(self.open_port)
        self.actionDesconectar.triggered.connect(self.close_port)
        self.actionLimpar.triggered.connect(self.clear_log)
        self.actionSair.triggered.connect(self.close_app)
        self.action_sobre.triggered.connect(self.about_this)

        self.setWindowIcon(QtGui.QIcon("../images/serial.png"))

        self.update_status_bar("Aplicação iniciada")
        self.create_styles_menu()

    def create_styles_menu(self):
        styles = QtWidgets.QStyleFactory.keys()
        print(styles[0])
        menu_bar = self.menuBar()
        menu_styles = menu_bar.addMenu("Styles")

        act_adwaita = QtWidgets.QAction("adwaita", self)
        act_adwaita.triggered.connect(lambda: self.change_style("adwaita"))
        act_Breeze = QtWidgets.QAction("Breeze", self)
        act_Breeze.triggered.connect(lambda: self.change_style("Breeze"))
        act_Oxygen = QtWidgets.QAction("Oxygen", self)
        act_Oxygen.triggered.connect(lambda: self.change_style("Oxygen"))
        act_QtCurve = QtWidgets.QAction("QtCurve", self)
        act_QtCurve.triggered.connect(lambda: self.change_style("QtCurve"))
        act_Windows = QtWidgets.QAction("Windows", self)
        act_Windows.triggered.connect(lambda: self.change_style("Windows"))
        act_Fusion = QtWidgets.QAction("Fusion", self)
        act_Fusion.triggered.connect(lambda: self.change_style("Fusion"))

        menu_styles.addAction(act_adwaita)
        menu_styles.addAction(act_Breeze)
        menu_styles.addAction(act_Oxygen)
        menu_styles.addAction(act_QtCurve)
        menu_styles.addAction(act_Windows)
        menu_styles.addAction(act_Fusion)

    def change_style(self, style):
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(style))
        print(style)

    def reload_ports(self):
        self.combo_box_portas.clear()
        portas = serial.tools.list_ports.comports()
        for p in portas:
            self.combo_box_portas.addItem(p.device)
        self.combo_box_portas.setCurrentIndex(1)

    def open_port(self):
        port_name = self.combo_box_portas.currentText()
        baud = self.combo_box_bauds.currentText()

        self.arduino = SerialThread(port_name, baud)
        self.arduino.signal.connect(self.text_log.append)
        self.arduino.start()

        if self.arduino.isRunning:
            self.actionConectar.setDisabled(True)
            self.actionAtualizar.setDisabled(True)
            self.combo_box_portas.setDisabled(True)
            self.combo_box_bauds.setDisabled(True)
            self.actionDesconectar.setEnabled(True)
            self.update_status_bar("Porta aberta: {}".format(
                self.arduino.port_name))

    def close_port(self):
        if self.arduino.isRunning():
            self.arduino.stop_work()
            self.arduino.close_port()
            self.actionConectar.setEnabled(True)
            self.actionAtualizar.setEnabled(True)
            self.combo_box_portas.setEnabled(True)
            self.combo_box_bauds.setEnabled(True)
            self.actionDesconectar.setDisabled(True)
            self.update_status_bar("Conexão encerrada: {} está offline.".format(
                self.arduino.port_name))

    def close_app(self):
        if self.arduino is not None:
            self.close_port()
        self.close()

    def clear_log(self):
        """
        Limpa o textEdit.
        """
        self.text_log.clear()
        self.update_status_bar("Log limpo.")

    def about_this(self):
        msg = """<font face="Consolas">Muito obrigado por usar nossa aplicação!</font>
                 <p>Essa aplicação monitora dados vindos de uma porta serial.</p>
                 <p>autor: @dfso</p>
                 <p>versão do software: 1.1x Junho/2018</p>
                 <p>Visite-nos em: <a href="https://github.com/dfso">Github @dfso</a></p>
                 <p>Ícones disponíveis em: 
                 <a href="https://icons8.com/">https://icons8.com/</a></p>"""

        QtWidgets.QMessageBox.about(self, "Sobre...", msg)

    def update_status_bar(self, msg):
        """[Atualiza as mensagens na barra de status.]

        Arguments:
            msg {str} -- [a mensagem a ser exibida.]
        """
        status_bar = self.statusBar()
        status_bar.showMessage(msg)

    def __del__(self):
        print("Aplicação encerrada.")


app = QtWidgets.QApplication(sys.argv)
my_window = App()
my_window.show()
sys.exit(app.exec_())

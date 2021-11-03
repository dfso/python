# coding: utf-8

import sys
from PyQt5 import QtWidgets

import gui
import serial_tool
import my_threads


class App(gui.MyWindow):

    dispositivo = None
    read_thread = None
    write_thread = None

    def __init__(self):
        super().__init__()
        self.setup_ui(self)

        print(QtWidgets.QStyleFactory.keys())

        self.btn_desconectar.setDisabled(True)
        self.line_cmd.setDisabled(True)

        self.btn_reload_ports.clicked.connect(self.reload_ports)
        self.btn_sair.clicked.connect(self.close_app)
        self.btn_conectar.clicked.connect(self.conectar)
        self.btn_desconectar.clicked.connect(self.desconectar)

        self.line_cmd.returnPressed.connect(self.enviar_comando)

        self.reload_ports()

    def conectar(self):
        self.dispositivo = serial_tool.SerialTool.conectar(
            self.combo_portas.currentText(),
            self.combo_bauds.currentText())
        if self.dispositivo.is_open:
            print("Conexão estabelecida.")
            self.btn_conectar.setDisabled(True)
            self.btn_desconectar.setEnabled(True)
            self.line_cmd.setEnabled(True)

        self.read_thread = my_threads.ReadThread(self.dispositivo)
        self.read_thread.signal.connect(self.text_log.append)
        self.read_thread.start()

    def desconectar(self):
        self.read_thread.stop_work()
        self.dispositivo.close()
        
        if self.write_thread is None:
            pass
        else:
            self.write_thread.stop_work()

        if not self.dispositivo.is_open:
            print("Conexão encerrada.")
            self.btn_desconectar.setDisabled(True)
            self.btn_conectar.setEnabled(True)
            self.line_cmd.setDisabled(True)

    def enviar_comando(self):
        self.write_thread = my_threads.WriteThread(self.dispositivo, self.line_cmd.text().upper())
        self.write_thread.start()
        self.text_log.append("<b><font color = green>Comando: "
                             + self.line_cmd.text().upper() + "</font></b>")

    def reload_ports(self):
        """
        Carrega no combobox os nomes do dispositivos.

        :return:
        """
        self.combo_portas.clear()
        portas = serial_tool.SerialTool.listar_portas()
        self.combo_portas.addItems(portas)
        self.combo_portas.setCurrentIndex(1)

    def close_app(self):
        if self.dispositivo is not None:
            self.desconectar()
        print("Aplicação encerrada.")
        self.close()


app = QtWidgets.QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())

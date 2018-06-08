import sys
from PyQt5 import QtWidgets, QtGui, QtCore

import gui
import serial_tool
import serial_thread_read
import serial_thread_write

class App(gui.MyWindow):

    arduino = None
    device = None
    cmds = []
    item = 0
    
    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        self.reload_ports()

        self.line_cmd.setDisabled(True)

        self.line_cmd.returnPressed.connect(self.send_cmd)
        self.btn_reload_ports.clicked.connect(self.reload_ports)

        self.btn_conectar.clicked.connect(self.open_port)
        self.btn_desconectar.clicked.connect(self.close_port)
        self.btn_sair.clicked.connect(self.close_app)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            print(self.item)
            print(len(self.cmds))
            print("key_Up pressed")
            try:
                self.line_cmd.setText(self.cmds[self.item-1])
                self.item = self.item - 1
            except IndexError as err:
                print(err)
                self.item = len(self.cmds)
        else:
            pass
    
    def open_port(self):
        port_name = self.combo_portas.currentText()
        baud = self.combo_bauds.currentText()

        self.arduino = serial_thread_read.SerialThreadRead(port_name, baud)
        self.arduino.open_port()
        self.line_cmd.setEnabled(True)
        self.btn_conectar.setDisabled(True)
        self.btn_desconectar.setEnabled(True)

        self.arduino.signal.connect(self.text_log.append)
        self.arduino.start()
        if self.arduino.isRunning():
            self.text_log.append("Conexão estabelecida.")
    
    def close_port(self):
        if self.arduino.isRunning():
            self.arduino.stop_work()
            self.arduino.close_port()
            self.line_cmd.setDisabled(True)
            self.btn_desconectar.setDisabled(True)
            self.btn_conectar.setEnabled(True)
        
        if self.device is not None and self.device.isRunning():
            self.device.stop_work()

        if self.arduino.isFinished():
            self.text_log.append("Conexão encerrada.")

    def close_app(self):
        if self.arduino is not None:
            self.close_port()
        self.close()
        print("Aplicação encerrada.")

    def __del__(self):
        self.close_app()

    
    def send_cmd(self):

        self.device = serial_thread_write.SerialThreadWrite(
            self.arduino.device, self.line_cmd.text())
        if self.device.isRunning():
            self.device.stop_work()
        self.device.start()

        self.text_log.append(self.line_cmd.text())
        if self.line_cmd.text() not in self.cmds:
            self.cmds.append(self.line_cmd.text())
            self.item = self.item + 1
        self.line_cmd.clear()
    
    def reload_ports(self):
        self.combo_portas.clear()
        portas = serial_tool.SerialTool.listar_portas()
        self.combo_portas.addItems(portas)
        self.combo_portas.setCurrentIndex(1)
        print(portas)

        



app = QtWidgets.QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())
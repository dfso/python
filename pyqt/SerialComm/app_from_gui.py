import sys
from PyQt5 import QtWidgets

import gui
import serial_tool

class App(gui.MyWindow):
    
    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        portas = serial_tool.SerialTool.listar_portas()
        self.combo_portas.addItems(portas)

app = QtWidgets.QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())
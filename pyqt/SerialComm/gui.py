import sys

from PyQt5 import QtWidgets, QtCore, QtGui


class MyWindow(QtWidgets.QWidget):

    def setup_ui(self, window):
        self.setGeometry(200, 200, 720, 480)
        self.setWindowTitle("PyQt5 Serial Controller @dfso")

        self.vbox_root = QtWidgets.QVBoxLayout()  # layout root

        self.hbox_conexao = QtWidgets.QHBoxLayout()
        self.group_device = QtWidgets.QGroupBox()
        self.group_device.setTitle("Conexão")
        self.label_portas = QtWidgets.QLabel("Dispositivos")
        self.combo_portas = QtWidgets.QComboBox()
        self.label_bauds = QtWidgets.QLabel("Baud Rate")
        self.combo_bauds = QtWidgets.QComboBox()
        self.bauds = ['9600', '115200']
        self.combo_bauds.addItems(self.bauds)
        self.group_grid = QtWidgets.QGridLayout(self.group_device)
        self.group_grid.addWidget(self.label_portas, 0, 0, 1, 1)
        self.group_grid.addWidget(self.combo_portas, 0, 1, 1, 1)
        self.group_grid.addWidget(self.label_bauds, 1, 0, 1, 1)
        self.group_grid.addWidget(self.combo_bauds, 1, 1, 1, 1)

        grid_btns = QtWidgets.QGridLayout()
        self.btn_conectar = QtWidgets.QPushButton("Conectar")
        self.btn_desconectar = QtWidgets.QPushButton("Desconectar")
        self.btn_reload_ports = QtWidgets.QPushButton("Reload")
        grid_btns.addWidget(self.btn_conectar, 0, 0, 1, 2)
        grid_btns.addWidget(self.btn_desconectar, 1, 1, 1, 1)
        grid_btns.addWidget(self.btn_reload_ports, 1, 0, 1, 1)

        self.hbox_conexao.addWidget(self.group_device)
        self.hbox_conexao.addLayout(grid_btns)

        form_layout_cmd = QtWidgets.QFormLayout()
        self.line_cmd = QtWidgets.QLineEdit()
        self.line_cmd.setPlaceholderText("Entre com um comando")
        form_layout_cmd.addRow(QtWidgets.QLabel("Comando"), self.line_cmd)

        hbox_edit = QtWidgets.QHBoxLayout()
        self.scroll_area = QtWidgets.QScrollArea()

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)

        self.text_log = QtWidgets.QTextEdit(self.scroll_area)
        # self.text_log.setFont(font)
        window.setFont(font)
        self.text_log.setReadOnly(True)
        hbox_edit.addWidget(self.text_log)

        self.btn_sair = QtWidgets.QPushButton("Sair")

        self.vbox_root.addLayout(self.hbox_conexao)
        self.vbox_root.addLayout(form_layout_cmd)
        self.vbox_root.addLayout(hbox_edit)
        self.vbox_root.addWidget(self.btn_sair, 0, QtCore.Qt.AlignRight)
        self.setLayout(self.vbox_root)

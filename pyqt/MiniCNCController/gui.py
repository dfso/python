# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    images_path = "./images/"

    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Mini CNC Controller @dfso")
        MainWindow.setWindowIcon(QtGui.QIcon("./images/cnc.png"))
        MainWindow.resize(893, 513)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        centralwidget = QtWidgets.QWidget(MainWindow)
        verticalLayout_2 = QtWidgets.QVBoxLayout(centralwidget)
        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.setContentsMargins(2, -1, 2, -1)
        horizontalLayout.setSpacing(5)
        group_conexao = QtWidgets.QGroupBox("Conexão", centralwidget)
        group_conexao.setMaximumSize(QtCore.QSize(16777215, 150))
        formLayout = QtWidgets.QFormLayout(group_conexao)
        formLayout.setLabelAlignment(QtCore.Qt.AlignLeft)
        formLayout.setFieldGrowthPolicy(
            QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        label_porta = QtWidgets.QLabel("<b>Porta</b>", group_conexao)
        self.combo_portas = QtWidgets.QComboBox(group_conexao)
        formLayout.addRow(label_porta, self.combo_portas)
        label_bauds = QtWidgets.QLabel("<b>Baud Rate</b>", group_conexao)
        self.combo_bauds = QtWidgets.QComboBox(group_conexao)
        bauds = ["9600", "115200"]
        self.combo_bauds.addItems(bauds)
        formLayout.addRow(label_bauds, self.combo_bauds)

        label_status_port = QtWidgets.QLabel(
            "<b><font color=blue>Estado da porta: </font></b>", group_conexao)
        self.label_estado_porta = QtWidgets.QLabel("...", group_conexao)
        formLayout.addRow(label_status_port, self.label_estado_porta)

        horizontalLayout.addWidget(group_conexao)
        group_jog = QtWidgets.QGroupBox("JOG", centralwidget)
        group_jog.setMaximumSize(QtCore.QSize(16777215, 150))
        gridLayout = QtWidgets.QGridLayout(group_jog)
        self.btn_z_recu = QtWidgets.QPushButton("Z", group_jog)
        gridLayout.addWidget(self.btn_z_recu, 2, 3, 1, 1)
        self.btn_y_recu = QtWidgets.QPushButton("Y", group_jog)
        gridLayout.addWidget(self.btn_y_recu, 2, 2, 1, 1)
        self.btn_home = QtWidgets.QPushButton("HOME", group_jog)
        gridLayout.addWidget(self.btn_home, 1, 2, 1, 1)
        self.btn_x_recu = QtWidgets.QPushButton("X", group_jog)
        gridLayout.addWidget(self.btn_x_recu, 1, 0, 1, 1)
        self.btn_x_avan = QtWidgets.QPushButton("X", group_jog)
        gridLayout.addWidget(self.btn_x_avan, 1, 3, 1, 1)
        self.btn_y_avan = QtWidgets.QPushButton("Y", group_jog)
        gridLayout.addWidget(self.btn_y_avan, 0, 2, 1, 1)
        self.btn_z_avan = QtWidgets.QPushButton("Z", group_jog)
        gridLayout.addWidget(self.btn_z_avan, 0, 3, 1, 1)

        label_step = QtWidgets.QLabel("Mover (mm)", group_jog)
        gridLayout.addWidget(label_step, 3, 0, 1, 1)
        self.radio_btn_mm = QtWidgets.QRadioButton("1mm", group_jog)
        self.radio_btn_mm.setChecked(True)
        gridLayout.addWidget(self.radio_btn_mm, 3, 2, 1, 1)
        self.radio_btn_dec_mm = QtWidgets.QRadioButton("0.1mm", group_jog)
        gridLayout.addWidget(self.radio_btn_dec_mm, 3, 3, 1, 1)

        horizontalLayout.addWidget(group_jog)
        group_posicao = QtWidgets.QGroupBox("Posição", centralwidget)
        group_posicao.setMaximumSize(QtCore.QSize(16777215, 150))
        formLayout_2 = QtWidgets.QFormLayout(group_posicao)
        formLayout_2.setFieldGrowthPolicy(
            QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        label_x = QtWidgets.QLabel("X", group_posicao)
        formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, label_x)
        self.lcd_x = QtWidgets.QLCDNumber(group_posicao)

        self.lcd_x.setSegmentStyle(QtWidgets.QLCDNumber.Flat)

        formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lcd_x)
        label_y = QtWidgets.QLabel("Y", group_posicao)
        formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, label_y)
        self.lcd_y = QtWidgets.QLCDNumber(group_posicao)

        self.lcd_y.setSegmentStyle(QtWidgets.QLCDNumber.Flat)

        formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lcd_y)
        label_z = QtWidgets.QLabel("Z", group_posicao)
        formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, label_z)
        self.lcd_z = QtWidgets.QLCDNumber(group_posicao)

        self.lcd_z.setSegmentStyle(QtWidgets.QLCDNumber.Flat)

        formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lcd_z)
        horizontalLayout.addWidget(group_posicao)
        verticalLayout_2.addLayout(horizontalLayout)
        verticalLayout = QtWidgets.QVBoxLayout()
        form_cmd = QtWidgets.QFormLayout()
        label_cmd = QtWidgets.QLabel("Comando", centralwidget)
        form_cmd.setWidget(0, QtWidgets.QFormLayout.LabelRole, label_cmd)
        self.line_cmd = QtWidgets.QLineEdit(centralwidget)
        self.line_cmd.setPlaceholderText("Aqui você envia os comandos para a MiniCNC")
        form_cmd.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_cmd)
        verticalLayout.addLayout(form_cmd)
        self.tabWidget = QtWidgets.QTabWidget(centralwidget)
        self.tab_log = QtWidgets.QWidget()
        horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_log)
        self.text_log = QtWidgets.QTextEdit(self.tab_log)
        self.text_log.setReadOnly(True)
        horizontalLayout_2.addWidget(self.text_log)
        self.tabWidget.addTab(self.tab_log, "Log")
        self.tab_cmds = QtWidgets.QWidget()
        verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_cmds)
        self.list_comandos = QtWidgets.QListView(self.tab_cmds)
        verticalLayout_3.addWidget(self.list_comandos)
        self.tabWidget.addTab(self.tab_cmds, "Comandos")
        verticalLayout.addWidget(self.tabWidget)
        verticalLayout_2.addLayout(verticalLayout)
        MainWindow.setCentralWidget(centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)

        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.actionConectar = QtWidgets.QAction(
            QtGui.QIcon(self.images_path + "connected.png"), "Conectar", MainWindow)
        self.actionDesconectar = QtWidgets.QAction(
            QtGui.QIcon(self.images_path + "disconnected.png"), "Desconectar", MainWindow)
        self.actionReload = QtWidgets.QAction(
            QtGui.QIcon(self.images_path + "update.png"), "Reload", MainWindow)
        self.action_sair = QtWidgets.QAction(
            QtGui.QIcon(self.images_path + "sair.png"), "Sair", MainWindow)
        self.action_about = QtWidgets.QAction(
            QtGui.QIcon(self.images_path + "sobre.png"), "Sobre", MainWindow)

        self.actionConectar.setShortcut("F2")
        self.actionConectar.setToolTip(
            "<b>Conectar<font color=#009688>[F2]</font></b>")
        self.actionDesconectar.setShortcut("F4")
        self.actionDesconectar.setToolTip(
            "<b>Desconectar<font color=red>[F4]</font></b>")
        self.actionReload.setShortcut("F5")
        self.actionReload.setToolTip(
            "<b>Recareregar lista de portas<font color=#009688>[F5]</font></b>")
        self.action_sair.setShortcut("Ctrl+Q")
        self.action_sair.setToolTip(
            "<b>Sair<font color=red>[Ctrl+Q]</font></b>")
        self.action_about.setShortcut("F1")
        self.action_about.setToolTip(
            "<b>Sobre<Font color=#009688>[F1]</font></b>"
        )


        self.menu_log = self.menubar.addMenu("&Log")
        self.action_limpar = QtWidgets.QAction(
            QtGui.QIcon(self.images_path + "limpar.png"), "Limpar", MainWindow)
        self.action_limpar.setShortcut("Ctrl+L")
        self.action_limpar.setToolTip(
            "<b>Limpar o log<font color=red>[Ctrl+L]</font></b>")
        self.menu_log.addAction(self.action_limpar)

        self.toolBar.addAction(self.actionConectar)
        self.toolBar.addAction(self.actionDesconectar)
        self.toolBar.addAction(self.actionReload)
        self.toolBar.addAction(self.action_about)
        self.toolBar.addAction(self.action_sair)

        self.btn_x_avan.setIcon(QtGui.QIcon(self.images_path + "x+.png"))
        self.btn_x_recu.setIcon(QtGui.QIcon(self.images_path + "x-.png"))
        self.btn_y_avan.setIcon(QtGui.QIcon(self.images_path + "y+.png"))
        self.btn_y_recu.setIcon(QtGui.QIcon(self.images_path + "y-.png"))
        self.btn_z_avan.setIcon(QtGui.QIcon(self.images_path + "z+.png"))
        self.btn_z_recu.setIcon(QtGui.QIcon(self.images_path + "z-.png"))
        self.btn_home.setIcon(QtGui.QIcon(self.images_path + "home.png"))

        self.tabWidget.setCurrentIndex(0)

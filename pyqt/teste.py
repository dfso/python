# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 571, 60))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.btn_download = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_download.setObjectName("btn_download")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_download)
        self.progressBar = QtWidgets.QProgressBar(self.formLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.progressBar)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox_temas = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_temas.setObjectName("comboBox_temas")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_temas)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 420, 591, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_sair = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_sair.setObjectName("btn_sair")
        self.horizontalLayout.addWidget(self.btn_sair)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_sair.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Teste PyQt"))
        self.btn_download.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "Selecione o tema"))
        self.btn_sair.setText(_translate("MainWindow", "&Sair"))
        temas = QtWidgets.QStyleFactory.keys()
        for t in temas:
            self.comboBox_temas.addItem(t)
        print(temas)
        

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


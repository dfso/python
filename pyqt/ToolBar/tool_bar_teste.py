import sys

from PyQt5 import QtGui, QtWidgets, QtCore
import PyQt5


class MyToolBar(QtWidgets.QMainWindow):

    imgs_path = "../images/"

    def __init__(self):
        super().__init__()

        self.titulo = "PyQt5 ToolBar @dfso"
        self.top = 100
        self.left = 100
        self.largura = 640
        self.altura = 400

        self.init_UI()
    
    def init_UI(self):

        self.setWindowTitle(self.titulo)
        self.setWindowIcon(QtGui.QIcon(self.imgs_path + "app.png"))
        self.setGeometry(self.top, self.left, self.largura, self.altura)

        self.create_toolbar()
        self.show()

    def create_toolbar(self):

        tool_bar = self.addToolBar("ToolBar")
        tool_bar.setIconSize(QtCore.QSize(48, 48))
        
        action_open = QtWidgets.QAction(QtGui.QIcon(self.imgs_path + "open.png"), "Abrir", self)
        action_open.setShortcut("Ctrl+O")

        action_new = QtWidgets.QAction(QtGui.QIcon(self.imgs_path + "new.png"), "Novo", self)
        action_new.setShortcut("Ctrl+N")

        action_save= QtWidgets.QAction(QtGui.QIcon(self.imgs_path + "save.png"), "Salvar", self)
        action_save.setShortcut("Ctrl+S")

        action_copy= QtWidgets.QAction(QtGui.QIcon(self.imgs_path + "copy.png"), "Copiar", self)
        action_copy.setShortcut("Ctrl+C")

        action_paste= QtWidgets.QAction(QtGui.QIcon(self.imgs_path + "paste.png"), "Colar", self)
        action_paste.setShortcut("Ctrl+V")

        action_delete= QtWidgets.QAction(QtGui.QIcon(self.imgs_path + "excluir.png"), "Deletar", self)
        action_delete.setShortcut("Delete")
        action_delete.triggered.connect(self.delete)

        action_sair = QtWidgets.QAction(QtGui.QIcon(self.imgs_path + "sair.png"), "Sair", self)
        action_sair.setShortcut("Ctrl+Q")
        action_sair.triggered.connect(self.sair)

        action_sobre = QtWidgets.QAction(QtGui.QIcon(self.imgs_path + "sobre.png"), "Sobre", self)
        action_sobre.setShortcut("F12")
        action_sobre.triggered.connect(self.sobre)
        
        tool_bar.addAction(action_open)
        tool_bar.addAction(action_new)
        tool_bar.addAction(action_save)
        tool_bar.addAction(action_copy)
        tool_bar.addAction(action_paste)
        tool_bar.addAction(action_delete)
        tool_bar.addAction(action_sair)
        tool_bar.addAction(action_sobre)
    
    def delete(self):
        print("delete")
    
    def sair(self):
        QtWidgets.QApplication.exit()
    
    def sobre(self):
        msg = """<h3><font face="Consolas">Muito obrigado por usar nossa aplicação!<h3>
                 <h3>autor: @dfso</h3>
                 <h3>versão do software: 1.00a</h3>
                 <p>Visite-nos em: <a href="https://github.com/dfso">Github @dfso</a></p>"""
        QtWidgets.QMessageBox.about(self, "Sobre", msg)


app = QtWidgets.QApplication(sys.argv)
m = MyToolBar()
sys.exit(app.exec())


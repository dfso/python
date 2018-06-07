from PyQt5 import QtGui, QtWidgets
import sys

class MyMenuBar(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.titulo = "PyQt5 MenuBar @dfso"
        self.top = 100
        self.left = 100
        self.largura = 640
        self.altura = 400

        self.init_UI()
    
    def init_UI(self):

        self.setWindowTitle(self.titulo)
        self.setWindowIcon(QtGui.QIcon("./images/app.png"))
        self.setGeometry(self.top, self.left, self.largura, self.altura)
        self.create_menubar()
        self.show()

    def create_menubar(self):

        menu_bar = self.menuBar()
        menu_arquivo = menu_bar.addMenu("Arquivo")
        menu_sobre = menu_bar.addMenu("Sobre...")
        
        action_sair = QtWidgets.QAction(QtGui.QIcon("./images/sair.png"), "Sair", self)
        action_sair.setShortcut("Ctrl+Q")
        action_sair.triggered.connect(self.sair)

        action_sobre = QtWidgets.QAction(QtGui.QIcon("./images/sobre.png"), "Sobre", self)
        action_sobre.setShortcut("F12")
        action_sobre.triggered.connect(self.sobre)

        menu_arquivo.addAction(action_sair)
        menu_sobre.addAction(action_sobre)
    
    def sair(self):
        QtWidgets.QApplication.exit()
    
    def sobre(self):
        msg = """<h3>Muito obrigado por usar nossa aplicação!<h3>
                 <h3>autor: @dfso</h3>
                 <h3>versão do software: 1.00a</h3>
                 <p>Visite-nos em: <a href="https://github.com/dfso">Github @dfso</a></p>"""
        QtWidgets.QMessageBox.about(self, "Sobre", msg)


app = QtWidgets.QApplication(sys.argv)
m = MyMenuBar()
sys.exit(app.exec())

        
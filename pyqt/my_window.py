from PyQt5 import QtGui, QtWidgets
import sys

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.titulo = "PyQt5 Window @dfso"
        self.top = 100
        self.left = 100
        self.largura = 640
        self.altura = 400
        self.init_UI()
    
    def init_UI(self):

        self.setWindowTitle(self.titulo)
        self.setWindowIcon(QtGui.QIcon("./images/app.png"))
        self.setGeometry(self.top, self.left, self.largura, self.altura)
        self.show()


app = QtWidgets.QApplication(sys.argv)
m = MyWindow()
sys.exit(app.exec())

        
import psutil
import sys
import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal

import thread_gui

class App(QtWidgets.QMainWindow, thread_gui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.cpu_progressBar.setValue(0)
        self.thread_class = ThreadClass()
        self.thread_class.start()
        self.thread_class.update_progressbar.connect(self.update_progressbar)

    def update_progressbar(self, val):
        self.cpu_progressBar.setValue(val)


class ThreadClass(QtCore.QThread):
    update_progressbar = pyqtSignal(int)

    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)
    
    def run(self):
        while True:
            val = int(psutil.cpu_percent(interval=1))
            self.update_progressbar.emit(val)
            print(val)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())



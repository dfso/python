from PyQt5 import QtCore


class ReadThread(QtCore.QThread):

    signal = QtCore.pyqtSignal(str)

    def __init__(self, dispositivo):
        super().__init__()

        self.dispositivo = dispositivo

    def run(self):
        print("Thread de leitura {} iniciada".format(
            self.currentThreadId()
        ))
        while True:
            data = self.dispositivo.readline().decode().strip()
            self.signal.emit(str(data))  # pipe
            print(data)

    def stop_work(self):
        self.terminate()
        self.wait()
        if self.isFinished():
            print("Thread de leitura finalizada.")


class WriteThread(QtCore.QThread):

    def __init__(self, dispositivo, data):
        super().__init__()

        self.dispositivo = dispositivo
        self.data = data + '\n'

    def run(self):
        print("Thread de escrita {} iniciada".format(
            self.currentThreadId()
        ))
        self.dispositivo.write(self.data.encode())
        print(self.data)

    def stop_work(self):
        self.terminate()
        self.wait()
        if self.isFinished():
            print("Thread de escrita finalizada.")

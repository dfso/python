import sys
from PyQt5 import QtWidgets
import threading
import serial
import monitor_ui


class App(monitor_ui.MonitorUI):

    arduino = None
    running = False

    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        self.running = True
        self.conectar()

        print(self.get_alive_threads())
        print(self.get_current_thread())

        self.thread = threading.Thread(
            name="thread_temp", target=self.update_temp, args=())
        self.thread.start()
        print(self.get_alive_threads())

    def conectar(self):
        self.arduino = serial.Serial('/dev/ttyUSB0', 9600)
        if self.arduino:
            print('Conexão estabelecida.')

    def update_temp(self):
        while self.arduino.isOpen() and self.running:
            data = self.arduino.readline().decode().strip()
            print(data)
            self.label_temp.setText(data)

    def desconectar(self):
        self.running = False
        self.thread.join()
        self.arduino.close()
        print(self.get_alive_threads())
        if not self.arduino.is_open:
            print('Conexão encerrada.')

    def get_alive_threads(self):
        return(f"""total de threads ativas: {threading.active_count()}\nthreads: {threading.enumerate()}""")

    def get_current_thread(self):
        return(f"thread atual: {threading.current_thread()}")

    # trata o evento de fechar a aplicação
    def closeEvent(self, event):
        print('saindo...')
        self.desconectar()
        event.accept()


app = QtWidgets.QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())

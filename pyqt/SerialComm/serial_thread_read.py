# -*- coding: utf-8 -*-

import serial
from serial import SerialException

from PyQt5 import QtCore


class SerialThreadRead(QtCore.QThread):

    device = None
    signal = QtCore.pyqtSignal(str)
    connected = False

    
    def __init__(self, port, baud):
        super().__init__()

        self.port_name = port
        self.baud = baud
        self.open_port()
    
    def run(self):
        print("Thread {} leitura iniciada".format(self.currentThreadId()))
        while True:
            data = self.device.readline().decode().strip()
            self.signal.emit(str(data)) # pipe
            print(data.strip())
    
    def open_port(self):
        try:
            self.device = serial.Serial(self.port_name, self.baud)
            print("Conexão estabelecida.")
            self.connected = True
        except SerialException as ex:
            print("[read]Um erro ocorreu: {}".format(ex))
    
    def close_port(self):
        if self.device.is_open:
            self.device.close()
            self.connected = False
            print("Porta offline.")
    
    def stop_work(self):
        self.terminate()
        self.wait()
        if self.isFinished():
            print("Thread de leitura finalizada.")
        

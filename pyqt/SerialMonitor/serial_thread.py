# -*- coding: utf-8 -*-

import serial
from serial import SerialException

from PyQt5 import QtCore


class SerialThread(QtCore.QThread):

    arduino = None
    signal = QtCore.pyqtSignal(str)
    port_name = ""
    baud = 0
    
    def __init__(self, port, baud):
        super().__init__()

        self.port_name = port
        self.baud = baud
    
        self.arduino = serial.Serial(self.port_name, self.baud)
        self.arduino.close()
    
    def run(self):
        print("Thread iniciada.")
        while True:
            data = self.arduino.readline().decode().strip()
            self.signal.emit(str(data)) # pipe
            print(data.strip())
    
    def open_port(self):
        try:
            self.arduino.open()
            print("Conexão estabelecida.")
        except SerialException as ex:
            print("Um erro ocorreu: {}".format(ex))
    
    def close_port(self):
        if self.arduino.is_open:
            self.arduino.close()
            print("Porta offline.")
    
    def stop_work(self):
        self.terminate()
        self.wait()
        if self.isFinished():
            print("Thread finalizada.")

    def send_data(self):
        self.arduino.write(b"A")    # one byte
        

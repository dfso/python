# -*- coding: utf-8 -*-

import serial
from serial import SerialException

from PyQt5 import QtCore


class SerialThreadWrite(QtCore.QThread):
    
    def __init__(self, device, cmd):
        super().__init__()

        self.device = device
        self.cmd = cmd+'\n'
    
    def run(self):
        print("Thread de escrita iniciada.")
        self.device.write(self.cmd.encode())
        #self.signal.emit(str(self.cmd)) # pipe
        print(self.cmd)
    
    def open_port(self):
        try:
            self.arduino.open()
            print("Conexão estabelecida.")
        except SerialException as ex:
            print("[write]Um erro ocorreu: {}".format(ex))
    
    def close_port(self):
        if self.arduino.is_open:
            self.arduino.close()
            print("Porta offline.")
    
    def stop_work(self):
        self.terminate()
        self.wait()
        if self.isFinished():
            print("Thread de escrita finalizada.")
    
        

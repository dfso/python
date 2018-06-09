# -*- coding: utf-8 -*-

import serial
from serial import SerialException

from PyQt5 import QtCore


class SerialThreadWrite(QtCore.QThread):
    
    def __init__(self, device, cmd):
        super().__init__()

        self.device = device
        self.cmd = cmd + '\n'
    
    def run(self):
        print("Thread {} de escrita iniciada".format(self.currentThreadId()))
        self.device.write(self.cmd.encode())
        print(self.cmd)
    
    def stop_work(self):
        self.terminate()
        self.wait()
        if self.isFinished():
            print("Thread de escrita finalizada.")
    
        

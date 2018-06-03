# -*- coding: utf-8 -*-
import threading
import time
import serial


class SerialThread(threading.Thread):

    def __init__(self, port_name, port_baud):

        threading.Thread.__init__(self)

        self.serial_port = None
        self.port = port_name
        self.baud = port_baud

        self.alive = threading.Event()
        # Start Thread
        self.alive.set()

    def obtem_dados(self):
        data = self.serial_port.readline().decode()
        print(data)
        
        return data

    def run(self):
        try:
            if self.serial_port:
                self.serial_port.close()

            self.serial_port = serial.Serial(self.port, self.baud)
            print(self.serial_port)

        except serial.SerialException:
            print("erro ao abrir dispositivo")
            return

        # Restart the clock
        #startTime = time.time()

        while self.alive.isSet():
            data = self.obtem_dados()
            print(data)

        # clean up
        if self.serial_port:
            self.serial_port.close()

    def join(self, timeout=None):
        self.alive.clear()
        threading.Thread.join(self, timeout)

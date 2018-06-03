# -*- coding: utf-8 -*-
import serial
import serial.tools.list_ports

from gi.repository import GLib

class Arduino:

    arduino = serial.Serial()
    tag = ""

    def abrir_porta(self, porta, baud):

        self.arduino = serial.Serial(porta, baud)

        print("Arduino online? {}".format(self.arduino.is_open))

        if self.arduino.inWaiting() > 0:
            self.arduino.flushInput()

        GLib.timeout_add(10, self.ler_dados)
        
    def ler_dados(self):
        while self.arduino.inWaiting() > 0:
            bytes = self.arduino.read(self.arduino.inWaiting())
            data = bytes.decode(encoding="utf-8", errors="strict")
            self.tag = data
            #print(data)
            print("valor de self.tag: {}".format(self.tag))

        return True

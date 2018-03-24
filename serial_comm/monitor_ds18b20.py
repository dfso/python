#!/usr/bin/python3
# -*- coding: utf-8 -*-
import serial
import serial.tools.list_ports

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, GObject

GLADE = "monitor_ds18b20.glade"
# cria a classe do programa
class MonitorDS18B20(Gtk.Window):

    arduino = serial.Serial()

    arduino_id = None

    builder = Gtk.Builder.new_from_file(GLADE)
    builder.add_from_file(GLADE)

    window = builder.get_object("window")

    comboPorts = builder.get_object("comboPorts")
    comboBauds = builder.get_object("comboBauds")
    btn_conectar = builder.get_object("btnConectar")
    btnSair = builder.get_object("btnSair")
    labelTemp = builder.get_object("labelTemp")

    def __init__(self):
        self.window.connect("destroy", Gtk.main_quit)

        self.btn_conectar.connect("clicked", self.open_port)
        self.btnSair.connect("clicked", self.sair)

        self.get_ports()

        self.window.show_all()

    def get_ports(self):
        ports = list(serial.tools.list_ports.comports())

        print("\n---------------------------------------------")
        print("\tPortas disponíveis")

        for p in ports:
            self.comboPorts.append_text(p[0])
            self.comboPorts.set_active(1)
            print(p[0])
        print("---------------------------------------------")

    def open_port(self, widget):
        if self.arduino_id:
            GLib.source_remove(self.arduino_id)
            self.arduino.close()

        port = self.comboPorts.get_active_text()
        baud = self.comboBauds.get_active_text()
        self.arduino = serial.Serial(port, baud)
        if self.arduino.inWaiting() > 0:
            self.arduino.flushInput()
        self.arduino_id = GLib.timeout_add(10, self.read_data)

        GLib.timeout_add(10, self.read_data)

    def read_data(self):
        while self.arduino.inWaiting() > 0:
            bytes = self.arduino.read(self.arduino.inWaiting())
            data = bytes.decode(encoding="utf-8", errors="strict")
            self.labelTemp.set_text(data)
            #end_iter = self.textbuffer.get_end_iter()
            #length = len(data)
            #self.textbuffer.insert(end_iter, data, length)

        return True

    def sair(self, widget):
        self.arduino.close()
        Gtk.main_quit()

    def __del__(self):
        print("tchau")

if __name__ == '__main__':
    application = MonitorDS18B20()
    Gtk.main()

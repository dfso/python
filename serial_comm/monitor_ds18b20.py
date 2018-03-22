#!/usr/bin/python3
# -*- coding: utf-8 -*-
import serial
import serial.tools.list_ports

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, GObject

# cria a classe do programa
class MonitorDS18B20(Gtk.Window):

    glade = "monitor_ds18b20.glade"

    arduino = serial.Serial()

    builder = Gtk.Builder.new_from_file(glade)
    builder.add_from_file(glade)

    window = builder.get_object("window")

    comboPorts = builder.get_object("comboPorts")
    comboBauds = builder.get_object("comboBauds")
    btn_conectar = builder.get_object("btnConectar")
    btnSair = builder.get_object("btnSair")
    labelTemp = builder.get_object("labelTemp")

    def get_ports(self):
        ports = list(serial.tools.list_ports.comports())

        for p in ports:
            self.comboPorts.append_text(p[0])
            self.comboPorts.set_active(1)
            print(p[0])

    def open_port(self, widget):
        self.arduino.port = self.comboPorts.get_active_text()
        self.arduino.baud = self.comboBauds.get_active_text()
        self.arduino.open()
        if self.arduino.is_open:
            self.btn_conectar.set_sensitive(False)
            self.comboPorts.set_sensitive(False)
            self.comboBauds.set_sensitive(False)

        GLib.timeout_add_seconds(2, self.read_info)

    def read_info(self):
        temp = self.arduino.readline()
        print(temp)
        self.labelTemp.set_label("Temp: " + temp)
        return True

    def sair(self, widget):
        self.arduino.close()
        Gtk.main_quit()

    def __del__(self):
        print("tchau")

    def __init__(self):
        self.window.connect("destroy", Gtk.main_quit)

        self.btn_conectar.connect("clicked", self.open_port)
        self.btnSair.connect("clicked", self.sair)

        self.get_ports()

        self.window.show_all()

if __name__ == '__main__':
    application = MonitorDS18B20()
    Gtk.main()

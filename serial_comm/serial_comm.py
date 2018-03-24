#!/usr/bin/python3
# -*- coding: utf-8 -*-
import serial
import serial.tools.list_ports

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from gi.repository import GLib

GLADE = "serial_comm.glade"

# cria a classe do programa
class SerialComm(Gtk.Window):

    def __init__(self):

        self.builder = Gtk.Builder.new_from_file(GLADE)
        self.builder.add_from_file(GLADE)

        self.window = self.builder.get_object("window")
        self.window.connect("destroy", self.sair)

        self.arduino_id = None

        self.comboPorts = self.builder.get_object("comboPorts")
        self.comboBauds = self.builder.get_object("comboBauds")
        self.btn_conectar = self.builder.get_object("btnConectar")
        self.btnLimpar = self.builder.get_object("btnLimpar")

        self.btnLimpar.connect("clicked", self.limpar)
        self.btn_conectar.connect("clicked", self.open_port)

        self.textbuffer = self.builder.get_object("textbuffer")
        self.textview = self.builder.get_object("textview")

        self.get_ports()
        self.gtk_style()
        self.window.show_all()

    def sair(self, window):
        print("saindo...")
        try:
            self.arduino.close()
        except:
            print("nenhuma porta estava aberta..")
        Gtk.main_quit()

    def limpar(self, button):
        self.textbuffer.set_text('')


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

    def read_data(self):
        while self.arduino.inWaiting() > 0:
            bytes = self.arduino.read(self.arduino.inWaiting())
            data = bytes.decode(encoding="utf-8", errors="strict")
            end_iter = self.textbuffer.get_end_iter()
            length = len(data)
            self.textbuffer.insert(end_iter, data, length)

        return True

    def gtk_style(self):
        css = "style.css"
        style_provider = Gtk.CssProvider()
        style_provider.load_from_path(css)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

if __name__ == '__main__':
    application = SerialComm()
    Gtk.main()

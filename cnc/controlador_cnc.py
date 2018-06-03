#!/usr/bin/python3
# -*- coding: utf-8 -*-
import serial
import serial.tools.list_ports

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, GObject

GLADE = "/home/dfso/devel/python/cnc/cnc_control.glade"
# cria a classe do programa
class ControladorCNC(Gtk.Window):

    builder = Gtk.Builder()
    builder.add_from_file(GLADE)

    window = builder.get_object("window")

    combo_box_passo = builder.get_object("combo_box_passo")

    btn_sair = builder.get_object("btn_sair")
    btn_home = builder.get_object("btn_home")
    btn_x_avan = builder.get_object("btn_x_avan")
    text_log = builder.get_object("text_log")
    log = builder.get_object("log")

    def __init__(self):
        self.window.connect("destroy", Gtk.main_quit)

        self.btn_sair.connect("clicked", self.sair)
        self.btn_home.connect("clicked", self.go_home)
        self.btn_x_avan.connect("clicked", self.avancar_x)

        self.window.show_all()

    def sair(self, button):
        print("fechando...")
        Gtk.main_quit()

    def go_home(self, button):
        self.insert_log("[manual]: G0X0Y0Z0")
        
    def avancar_x(self, button):
        self.insert_log("[manual] G0X{}".format(self.combo_box_passo.get_active_text()))

    
    def insert_log(self, log):
        end_iter = self.log.get_end_iter()
        self.log.insert(end_iter, "{}{}".format(log, "\n"))

    def __del__(self):
        print("tchau")

if __name__ == '__main__':
    application = ControladorCNC()
    Gtk.main()

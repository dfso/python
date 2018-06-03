# -*- coding: utf-8 -*-

from arduino import Arduino

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, GObject


class Teste:

    def __init__(self):
        win = Gtk.Window()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()

        a = Arduino()
        a.abrir_porta("/dev/ttyUSB0", 9600)
        print("a.tag: {}".format(a.tag))

        

if __name__ == '__main__':
    t = Teste()    
    Gtk.main()
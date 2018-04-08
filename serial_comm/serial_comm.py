#!/usr/bin/python3
# -*- coding: utf-8 -*-
import serial
import serial.tools.list_ports

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from gi.repository import GLib

GLADE = "/home/dfso/devel/python/serial_comm/serial_comm.glade"

# cria a classe do programa
class SerialComm(Gtk.Window):
    ''' Uma aplicação que realiza a leitura de dados do arduino
     e exibe em um textview '''

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
        ''' fechas as conexões abertas e sai da aplicação '''
        print("saindo...")
        try:
            self.arduino.close()
        except:
            print("nenhuma porta estava aberta..")
        Gtk.main_quit()

    def limpar(self, button):
        ''' limpa o textbuffer do textview '''
        self.textbuffer.set_text('')


    def get_ports(self):
        ''' obtém as portas seriais do sistema e preenche o combobox
        com os nomes das portas '''
        ports = list(serial.tools.list_ports.comports())

        print("{:-^38}".format("")) #imprime o caracter '-' 38 vezes
        print("{:*^38}".format("Portas disponíveis"))

        for p in ports:
            self.comboPorts.append_text(p[0])
            self.comboPorts.set_active(1)
            print(p[0])
        print("{:-^38}".format(""))

    def open_port(self, widget):
        ''' abre a conexão com a placa e chama a função que lê os dados'''
        port = self.comboPorts.get_active_text()
        baud = self.comboBauds.get_active_text()
        self.arduino = serial.Serial(port, baud)

        if self.arduino.is_open:
            self.btn_conectar.set_sensitive(False)

        if self.arduino_id:
            GLib.source_remove(self.arduino_id)
            self.arduino.close()

        if self.arduino.inWaiting() > 0:
            self.arduino.flushInput()
        self.arduino_id = GLib.timeout_add(10, self.read_data)

    def read_data(self):
        ''' realiza a leitura dos dados vindos da placa '''
        while self.arduino.inWaiting() > 0:
            bytes = self.arduino.read(self.arduino.inWaiting())
            data = bytes.decode(encoding="utf-8", errors="strict")
            end_iter = self.textbuffer.get_end_iter()
            length = len(data)
            self.textbuffer.insert(end_iter, data, length)
            print(data) # para fins de debug

        return True

    def gtk_style(self):
        ''' aplica estilos nos componentes usando um arquivo .css '''

        css = "/home/dfso/devel/python/serial_comm/style.css"
        style_provider = Gtk.CssProvider()
        style_provider.load_from_path(css)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

if __name__ == '__main__':
    application = SerialComm()
    Gtk.main()

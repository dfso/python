#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       login.py
#       
#       Copyright 2011 Lucas P Brígida <lucasbrigida@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import pygtk
pygtk.require("2.0")
import gtk, gtk.glade
 
class Aplicacao:
  def __init__(self):
    treeWidgets = gtk.glade.XML('login.glade')
 
    #Associa os widgets a variaveis;
    #Os widgets que sao obtidos a partir de pedidos ao objeto 'arvoreDeWidgets'
    self.mainWindow = treeWidgets.get_widget('mainWindow')
    
    #Conecta Sinais aos Callbacks
    treeWidgets.signal_autoconnect(self)
  
    #Exibe toda interface
    self.mainWindow.show_all()
 
    #Inicia o loop principal de eventos (GTK MainLoop)
    gtk.main()
 
  #Callbacks
  def getLoginField(self,widget,data):
	   self.user=widget.get_text()

  def getPassField(self,widget,data):
	   self.passwd=widget.get_text()
    
  def quitMainWindow(self, widget, data):
    #Sai do loop principal de eventos, finalizando o programa
    gtk.main_quit()
 
  # Funções
  def login(self,widget,data):
	  diag=gtk.MessageDialog(self.mainWindow, gtk.DIALOG_MODAL,gtk.MESSAGE_INFO,gtk.BUTTONS_OK)
	  diag.set_markup("Login realizado com sucesso!")
	  diag.run()
	  diag.destroy()
  
 
#Inicia a aplicacao
if __name__ == "__main__":
  Aplicacao()

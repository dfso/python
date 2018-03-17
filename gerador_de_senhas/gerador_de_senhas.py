#!/usr/bin/python3
# -*- coding: utf-8 -*-

import gi
import random
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


# cria a classe do programa
class GeradorDeSenhas(Gtk.Window):

    glade = "gerador_de_senhas.glade"

    builder = Gtk.Builder.new_from_file(glade)
    builder.add_from_file(glade)

    clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

    entry_tamanho = builder.get_object("entry_tamanho")
    entry_saida = builder.get_object("entry_saida")
    btn_limpar = builder.get_object("btn_limpar")
    btn_copiar = builder.get_object("btn_copiar")

#==============================================================================
#   gera a tabela ascII
#==============================================================================
    def get_tabela(self):
        asc = []
        for i in range(33, 126):
            asc += chr(i)

        return asc

    def gerar_senha(self, button):

        tabela = self.get_tabela()
        try:
            #tamanho = int(self.entry_tamanho.get_text())
            tamanho = self.entry_tamanho.get_text()
            if not tamanho:
                print("tamanho não definido")
                return
            else:
                tamanho = int(tamanho)

        except ValueError as e:
            print("errou aqui: %s" % str(e))

        senha = ''

        try:
            for x in range(tamanho):
                senha += tabela[int(random.random() * 94)]
        except IndexError as erro:
            print("Erro: %s" % str(erro))
            senha = ''
            self.entry_saida.set_text(str(erro))
            pass

        print("Sua senha: %s" % senha)
        self.entry_saida.set_text(senha)

    def copy_to(self, widget):
        self.clipboard.set_text(self.entry_saida.get_text(), -1)
        print("Senha copiada para clipboard")

    def limpar(self, sinal):
        self.entry_saida.set_text("")

    def __init__(self):

        window = self.builder.get_object("janela")
        window.connect("delete-event", Gtk.main_quit)

        btn_gerar = self.builder.get_object("btn_gerar")
        btn_gerar.connect("clicked", self.gerar_senha)

        self.btn_copiar.connect("clicked", self.copy_to)

        self.btn_limpar.connect("clicked", self.limpar)

        self.entry_tamanho.connect("activate", self.gerar_senha)

        self.gtk_style()

        window.show_all()

    def gtk_style(self):

        css = "style.css"
        style_provider = Gtk.CssProvider()
        style_provider.load_from_path(css)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )


if __name__ == '__main__':
    programa = GeradorDeSenhas()
    Gtk.main()
